import logging
import sys
import time
import threading
from functools import wraps

from olo.errors import ORMError
from olo.logger import logger
from olo.utils import log_call


def lock(func):
    @wraps(func)
    def _(self, *args, **kwargs):
        with self.lock:
            return func(self, *args, **kwargs)

    return _


def log_pool(fmt):

    return log_call(
        '[POOL]: {}'.format(fmt),
        logger,
        level=logging.DEBUG,
        toggle=(
            lambda *args, **kwargs:
            len(args) > 0 and getattr(args[0], 'enable_log', False)
        )
    )


class ConnProxy(object):
    pid = 0

    def __init__(self, conn, pool):
        self.lock = threading.RLock()
        with self.lock:
            if self.__class__.pid >= sys.maxsize:
                self.__class__.pid = 0
            self.__class__.pid += 1
            self.id = self.__class__.pid
        self.conn = conn
        self.pool = pool
        self.expire_time = time.time() + pool.timeout
        self.is_closed = False

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __getattr__(self, item):
        return getattr(self.conn, item)

    def __str__(self):
        return '<ConnProxy id={}, conn={}, pool={}>'.format(
            self.id, self.conn, self.pool
        )

    __repr__ = __str__

    def close(self):
        self.is_closed = True
        self.release()
        self.conn.close()

    @property
    def is_expired(self):
        return self.expire_time <= time.time()

    def release(self):
        self.pool.release_conn(self)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.release()

    def ping(self):
        raise NotImplementedError


class Pool(object):
    def __init__(self,
                 creator,
                 timeout=60 * 60,
                 max_active_size=10,
                 max_idle_size=5,
                 tick_time=0.01,
                 wait_time=60 * 60,
                 conn_proxy_cls=ConnProxy,
                 enable_log=False):
        self.creator = creator
        self.timeout = timeout
        self.max_active_size = max_active_size
        self.max_idle_size = max_idle_size
        self.active_conns = []
        self.idle_conns = []
        self.lock = threading.RLock()
        self.tick_time = tick_time
        self.wait_time = wait_time
        self.conn_proxy_cls = conn_proxy_cls
        self.enable_log = enable_log

    def __str__(self):
        return (
            '<Pool active_size={}, idle_size={}, max_active_size={},'
            ' max_idle_size={}>'
        ).format(
            self.active_size, self.idle_size, self.max_active_size,
            self.max_idle_size)

    __repr__ = __str__

    @property
    def active_size(self):
        return len(self.active_conns)

    @property
    def idle_size(self):
        return len(self.idle_conns)

    def _create_conn(self):
        conn = self.creator()
        return self.conn_proxy_cls(conn, self)

    @log_pool('acquire conn: {%ret}')
    def acquire_conn(self):
        count = 0
        while True:
            with self.lock:
                if self.idle_conns:
                    conn = self.idle_conns.pop(0)
                    if not self.ping_conn(conn):
                        if count > 10:
                            raise ORMError('cannot get a alive connection!')
                        # FIXME
                        try:
                            self.destroy_conn(conn)
                        except Exception:
                            pass
                        count += 1
                        time.sleep(0.5)
                        return self.acquire_conn()
                    if conn.is_expired or conn.is_closed:
                        self.destroy_conn(conn)
                        return self.acquire_conn()
                    self.active_conns.append(conn)
                    return conn
                if len(self.active_conns) == self.max_active_size:
                    time.sleep(self.tick_time)
                    _conn = self.active_conns[0]
                    if time.time() - _conn.expire_time + self.timeout >= self.wait_time:  # noqa
                        raise ORMError('wait to release connection too long!')
                    continue
                conn = self._create_conn()
                self.active_conns.append(conn)
                return conn

    def ping_conn(self, conn):
        try:
            conn.ping()
            return True
        except Exception:
            return False

    @lock
    def clear_conns(self):
        while self.idle_conns:
            conn = self.idle_conns.pop()
            conn.close()
        while self.active_conns:
            conn = self.active_conns.pop()
            conn.close()

    @lock
    @log_pool('destroy conn: {conn}')
    def destroy_conn(self, conn):
        if conn in self.active_conns:
            self.active_conns.remove(conn)
        if conn in self.idle_conns:
            self.idle_conns.remove(conn)  # pragma: no cover
        if not conn.is_closed:
            conn.close()

    @lock
    @log_pool('release conn: {conn}')
    def release_conn(self, conn):
        if len(self.idle_conns) == self.max_idle_size or conn.is_closed or conn.is_expired:
            self.destroy_conn(conn)
            return
        if not conn.is_closed and conn not in self.idle_conns:
            self.idle_conns.append(conn)
        if conn in self.active_conns:
            self.active_conns.remove(conn)
