#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time
import threading
import base64
import pickle
import datetime
from hashlib import sha1
from copy import deepcopy

from .. import http, utils
from ..conf import settings
from ..db import client
from ..utils.datastructs import threadeddict
from ..utils.py3helpers import PY2, text_type, string_types

support_redis = True
try:
    import redis
except ImportError:
    support_redis = False


class SessionExpired(http.HTTPError):
    def __init__(self, message):
        http.HTTPError.__init__(self, '200 OK', {}, data=message)


class Session(object):
    """
    Session management
    """
    __slots__ = [
        "store",
        "_initializer",
        "_last_cleanup_time",
        "_config",
        "_data",
        "__getitem__",
        "__setitem__",
        "__delitem__",
    ]

    def __init__(self, app, initializer=None):
        self._initializer = initializer
        self._last_cleanup_time = 0
        self._data = threadeddict()

        self.__getitem__ = self._data.__getitem__
        self.__setitem__ = self._data.__setitem__
        self.__delitem__ = self._data.__delitem__

        self.store = self._loadStore()

        if app:
            app.add_processor(self._processor)

    def __contains__(self, name):
        return name in self._data

    def __getattr__(self, name):
        return getattr(self._data, name)

    def __setattr__(self, name, value):
        if name in self.__slots__:
            object.__setattr__(self, name, value)
        else:
            setattr(self._data, name, value)

    def __delattr__(self, name):
        delattr(self._data, name)

    def _processor(self, handler):
        """Application processor to setup session for every request"""
        self._cleanup()
        self._load()
        try:
            return handler()
        finally:
            self._save()

    def _loadStore(self):
        store_type = settings.SESSION_STORE
        store_config = settings.SESSION_STORE_CONFIG

        if store_type == 'DiskStore':
            assert isinstance(store_config, dict) == True
            root = store_config.get("path", "/tmp")
            store = DiskStore(root)
        elif store_type == 'DBStore':
            assert isinstance(store_config, dict) == True
            table_name = store_config.pop("TABLE_NAME", "session")
            db = client.Database(**store_config)
            store = DBStore(db, table_name)
        elif store_type == "RedisStore":
            assert isinstance(store_config, string_types) == True
            try:
                import redis
            except ImportError as e:
                raise ImportError("RedisStore need install redis module: {}".format(e))
            pool = redis.ConnectionPool.from_url(store_config)
            store = RedisStore(pool)
        elif store_type == 'ShelfStore':
            assert isinstance(store_config, dict) == True
            try:
                import shelve
            except ImportError as e:
                raise ImportError("ShelfStore need install shelve module: {}".format(e))
            shelf = shelve.open(store_config.get("path", "/tmp/session.shelf"))
            store = ShelfStore(shelf)
        else:
            raise AttributeError("SESSION_STORE {} is invaild.".format(store_type))
        return store

    def _load(self):
        """Load the session from the store, by the id from cookie"""
        cookie_name = settings.SESSION_COOKIE_NAME
        self.session_id = http.cookies().get(cookie_name)

        # protection against session_id tampering
        if self.session_id and not self._valid_session_id(self.session_id):
            self.session_id = None

        self._check_expiry()
        if self.session_id:
            d = self.store[self.session_id]
            self.update(d)
            self._validate_ip()

        if not self.session_id:
            self.session_id = self._generate_session_id()

            if self._initializer:
                if isinstance(self._initializer, dict):
                    self.update(deepcopy(self._initializer))
                elif hasattr(self._initializer, "__call__"):
                    self._initializer()

        self.ip = http.request.ip

    def _check_expiry(self):
        # check for expiry
        if self.session_id and self.session_id not in self.store:
            if settings.SESSION_COOKIE_IGNORE_EXPIRY:
                self.session_id = None
            else:
                return self.expired()

    def _validate_ip(self):
        # check for change of IP
        if self.session_id and self.get("ip", None) != http.request.ip:
            if not settings.SESSION_COOKIE_IGNORE_CHANGE_IP:
                return self.expired()

    def _save(self):
        current_values = dict(self._data)
        del current_values["session_id"]
        del current_values["ip"]

        if not self.get("_killed") and current_values != self._initializer:
            self._setcookie(self.session_id)
            self.store[self.session_id] = dict(self._data)
        else:
            if http.cookies().get(settings.SESSION_COOKIE_NAME):
                self._setcookie(
                    self.session_id,
                    expires=settings.SESSION_COOKIE_TIMEOUT,
                    samesite=settings.SESSION_COOKIE_SAMESITE,
                )

    def _setcookie(self, session_id, expires="", **kw):
        cookie_name = settings.SESSION_COOKIE_NAME
        cookie_domain = settings.SESSION_COOKIE_DOMAIN
        cookie_path = settings.SESSION_COOKIE_PATH
        httponly = settings.SESSION_COOKIE_HTTPONLY
        secure = settings.SESSION_COOKIE_SECURE
        samesite = kw.get("samesite", settings.SESSION_COOKIE_SAMESITE)
        http.setcookie(
            cookie_name,
            session_id,
            expires=expires or settings.SESSION_COOKIE_TIMEOUT,
            domain=cookie_domain,
            httponly=httponly,
            secure=secure,
            path=cookie_path,
            samesite=samesite,
        )

    def _generate_session_id(self):
        """Generate a random id for session"""

        while True:
            rand = os.urandom(16)
            now = time.time()
            secret_key = settings.SESSION_COOKIE_SECRET_KEY

            hashable = "%s%s%s%s" % (rand, now, utils.safestr(http.request.ip), secret_key)
            session_id = sha1(hashable if PY2 else hashable.encode("utf-8"))
            session_id = session_id.hexdigest()
            if session_id not in self.store:
                break
        return session_id

    def _valid_session_id(self, session_id):
        rx = utils.re_compile("^[0-9a-fA-F]+$")
        return rx.match(session_id)

    def _cleanup(self):
        """Cleanup the stored sessions"""
        current_time = time.time()
        timeout = settings.SESSION_COOKIE_TIMEOUT
        if current_time - self._last_cleanup_time > timeout:
            self.store.cleanup(timeout)
            self._last_cleanup_time = current_time

    def expired(self):
        """Called when an expired session is atime"""
        self._killed = True
        self._save()
        raise SessionExpired(settings.SESSION_COOKIE_EXPIRED_MESSAGE)

    def kill(self):
        """Kill the session, make it no longer available"""
        del self.store[self.session_id]
        self._killed = True


class Store:
    """Base class for session stores"""

    def __contains__(self, key):
        raise NotImplementedError()

    def __getitem__(self, key):
        raise NotImplementedError()

    def __setitem__(self, key, value):
        raise NotImplementedError()

    def cleanup(self, timeout):
        """removes all the expired sessions"""
        raise NotImplementedError()

    def encode(self, session_dict):
        """encodes session dict as a string"""
        pickled = pickle.dumps(session_dict)
        return base64.b64encode(pickled)

    def decode(self, session_data):
        """decodes the data to get back the session dict """
        pickled = base64.b64decode(session_data)
        return pickle.loads(pickled)


class DiskStore(Store):
    """
        Store for saving a session on disk.

        > import tempfile
        > root = tempfile.mkdtemp()
        > s = DiskStore(root)
        > s['a'] = 'foo'
        > s['a']
        'foo'
        > time.sleep(0.01)
        > s.cleanup(0.01)
        > s['a']
        Traceback (most recent call last):
            ...
        KeyError: 'a'
    """

    def __init__(self, root):
        # if the storage root doesn't exists, create it.
        if not os.path.exists(root):
            os.makedirs(os.path.abspath(root))
        self.root = root

    def _get_path(self, key):
        if os.path.sep in key:
            raise ValueError("Bad key: %s" % repr(key))
        return os.path.join(self.root, key)

    def __contains__(self, key):
        path = self._get_path(key)
        return os.path.exists(path)

    def __getitem__(self, key):
        path = self._get_path(key)

        if os.path.exists(path):
            with open(path, "rb") as fh:
                pickled = fh.read()
            try:
                return self.decode(pickled)
            except Exception:
                self.__delitem__(key)
        raise KeyError(key)

    def __setitem__(self, key, value):
        path = self._get_path(key)
        pickled = self.encode(value)
        try:
            tname = path + "." + threading.current_thread().getName()
            with open(tname, "wb") as f:
                f.write(pickled)
            os.rename(tname, path)
        except Exception:
            pass

    def __delitem__(self, key):
        path = self._get_path(key)
        if os.path.exists(path):
            os.remove(path)

    def cleanup(self, timeout):
        now = time.time()
        for f in os.listdir(self.root):
            path = self._get_path(f)
            atime = os.stat(path).st_atime
            if now - atime > timeout:
                os.remove(path)


class DBStore(Store):
    """Store for saving a session in database
    Needs a table with the following columns:

        session_id CHAR(128) UNIQUE NOT NULL,
        atime DATETIME NOT NULL default current_timestamp,
        data TEXT
    """

    def __init__(self, db, table_name):
        self.db = db
        self.table = table_name

    def __contains__(self, key):
        sql = "select session_id from {table} where session_id=?".format(table=self.table)
        ret = self.db.select(sql, key)
        if len(ret) == 2 and ret[0] == True:
            return bool(list(ret[1]))
        return False

    def __getitem__(self, key):
        now = datetime.datetime.now()
        sql = "select session_id, atime, data from {table} where session_id=?".format(table=self.table)
        try:
            ret = self.db.selectone(sql, key)
            if len(ret) == 2 and ret[0] == True:
                self.db.update(self.table, "session_id=?", key, atime=now)
        except IndexError:
            raise KeyError(key)
        else:
            try:
                return self.decode(ret[1].data)
            except ValueError:
                self.__delitem__(key)
        raise KeyError(key)

    def __setitem__(self, key, value):
        pickled = self.encode(value)
        now = datetime.datetime.now()
        if key in self:
            self.db.update(self.table, "session_id=?", key, data=pickled, atime=now)
        else:
            self.db.insert(self.table, session_id=key, atime=now, data=pickled)

    def __delitem__(self, key):
        self.db.delete(self.table, "session_id=?", key)

    def cleanup(self, timeout):
        timeout = datetime.timedelta(hours=(timeout / 3600))
        last_allowed_time = datetime.datetime.now() - timeout
        self.db.delete(self.table, "atime < ?", last_allowed_time)


class RedisStore(Store):
    """
            Store for saving a session on Redis.

            > import redis
            > pool = redis.ConnectionPool.from_url("redis://127.0.0.1:6379/0")
            > s = RedisStore(root)
            > s['a'] = 'foo'
            > s['a']
            'foo'
            > time.sleep(0.01)
            > s.cleanup(0.01)
            > s['a']
            Traceback (most recent call last):
                ...
            KeyError: 'a'
        """

    def __init__(self, pool):
        global support_redis
        assert support_redis == True

        self.conn = redis.Redis(connection_pool=pool)
        self.ex = settings.SESSION_COOKIE_TIMEOUT
        self.sid = settings.SESSION_COOKIE_NAME
        if not self.sid:
            self.sid = "LeafPy_session_id"

    def _safestr(self, s, encoding='utf-8'):
        t = type(s)
        if t is text_type:
            return s
        elif t is bytes:
            return s.decode(encoding)
        elif t in [int, float, bool]:
            return text_type(s)
        return text_type(s)

    def _genkey(self, key):
        return "{sid}:{key}".format(sid=self.sid, key=key)

    def _iskey(self, key):
        if self._safestr(key).startswith(self.sid):
            return True
        return False

    def __contains__(self, key):
        if self.conn.get(self._genkey(key)):
            return True
        return False

    def __getitem__(self, key):
        pickled = self.conn.get(self._genkey(key))
        if pickled:
            try:
                return self.decode(pickled)
            except Exception:
                self.__delitem__(key)
        raise KeyError(key)

    def __setitem__(self, key, value):
        pickled = self.encode(value)
        return self.conn.set(self._genkey(key), pickled, self.ex)

    def __delitem__(self, key):
        return self.conn.delete(self._genkey(key))

    def cleanup(self, timeout):
        pass  # needn't to clean, because redis set ex in setitem


class ShelfStore:
    """Store for saving session using `shelve` module.

        import shelve
        store = ShelfStore(shelve.open('session.shelf'))

    XXX: is shelve thread-safe?
    """

    def __init__(self, shelf):
        self.shelf = shelf

    def __contains__(self, key):
        return key in self.shelf

    def __getitem__(self, key):
        atime, v = self.shelf[key]
        self[key] = v  # update atime
        return v

    def __setitem__(self, key, value):
        self.shelf[key] = time.time(), value

    def __delitem__(self, key):
        try:
            del self.shelf[key]
        except KeyError:
            pass

    def cleanup(self, timeout):
        now = time.time()
        for k in self.shelf:
            atime, v = self.shelf[k]
            if now - atime > timeout:
                del self[k]
