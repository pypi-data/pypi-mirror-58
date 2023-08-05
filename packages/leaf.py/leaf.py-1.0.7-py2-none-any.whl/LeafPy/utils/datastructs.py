#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = [
    "Storage", "storage",
    "JsonDict", "jsondict",
    "AttrDict", "attrdict",
    "ThreadedDict", "threadeddict"
]

from threading import local as threadlocal

from ..utils.encoding import safeunicode
from ..utils.py3helpers import (
    iteritems,
    iterkeys,
    itervalues,
)


class Storage(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return "<Storage " + dict.__repr__(self) + ">"


storage = Storage


class JsonDict(Storage):
    def __repr__(self):
        return "<JsonDict " + dict.__repr__(self) + ">"


jsondict = JsonDict


class AttrDict(Storage):
    def __getattr__(self, key):
        if key in self:
            return self[key]
        return None

    def __repr__(self):
        return "<AttrDict " + dict.__repr__(self) + ">"


attrdict = AttrDict


def storify(mapping, *requireds, **defaults):
    _unicode = defaults.pop("_unicode", False)

    # if _unicode is callable object, use it convert a string to unicode.
    to_unicode = safeunicode
    if _unicode is not False and hasattr(_unicode, "__call__"):
        to_unicode = _unicode

    def unicodify(s):
        if _unicode and isinstance(s, str):
            return to_unicode(s)
        else:
            return s

    def getvalue(x):
        if hasattr(x, "file") and hasattr(x, "value"):
            return x.value
        elif hasattr(x, "value"):
            return unicodify(x.value)
        else:
            return unicodify(x)

    def intget(integer, default=None):
        try:
            return int(integer)
        except (TypeError, ValueError):
            return default or integer

    stor = Storage()
    for key in requireds + tuple(mapping.keys()):
        value = mapping[key]
        if isinstance(value, list):
            if isinstance(defaults.get(key), list):
                value = [getvalue(x) for x in value]
            else:
                value = value[-1]
        if not isinstance(defaults.get(key), dict):
            value = getvalue(value)
            if isinstance(defaults.get(key), int):
                value = intget(value)
        if isinstance(defaults.get(key), list) and not isinstance(value, list):
            value = [value]

        setattr(stor, key, value)

    for (key, value) in iteritems(defaults):
        result = value
        if hasattr(stor, key):
            result = stor[key]
        if value == () and not isinstance(result, tuple):
            result = (result,)
        setattr(stor, key, result)

    return stor


class ThreadedDict(threadlocal):
    """
    Thread local storage.

        > d = ThreadedDict()
        > d.x = 1
        > d.x
        1
        > import threading
        > def f(): d.x = 2
        ...
        > t = threading.Thread(target=f)
        > t.start()
        > t.join()
        > d.x
        1
    """

    _instances = set()

    def __init__(self):
        ThreadedDict._instances.add(self)

    def __del__(self):
        ThreadedDict._instances.remove(self)

    def __hash__(self):
        return id(self)

    def clear_all():
        """Clears all ThreadedDict instances.
        """
        for t in list(ThreadedDict._instances):
            t.clear()

    clear_all = staticmethod(clear_all)

    # Define all these methods to more or less fully emulate dict -- attribute access
    # is built into threading.local.

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __contains__(self, key):
        return key in self.__dict__

    has_key = __contains__

    def clear(self):
        self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def get(self, key, default=None):
        return self.__dict__.get(key, default)

    def items(self):
        return self.__dict__.items()

    def iteritems(self):
        return iteritems(self.__dict__)

    def keys(self):
        return self.__dict__.keys()

    def iterkeys(self):
        try:
            return iterkeys(self.__dict__)
        except NameError:
            return self.__dict__.keys()

    iter = iterkeys

    def values(self):
        return self.__dict__.values()

    def itervalues(self):
        return itervalues(self.__dict__)

    def pop(self, key, *args):
        return self.__dict__.pop(key, *args)

    def popitem(self):
        return self.__dict__.popitem()

    def setdefault(self, key, default=None):
        return self.__dict__.setdefault(key, default)

    def update(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)

    def __repr__(self):
        return "<ThreadedDict %r>" % self.__dict__

    __str__ = __repr__


threadeddict = ThreadedDict
