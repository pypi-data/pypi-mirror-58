#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import threading

from ..utils.datastructs import Storage
from ..utils.encoding import safestr
from ..utils.py3helpers import (
    string_types,
    iteritems
)

iters = [list, tuple, set, frozenset]


class _hack(tuple):
    """
    A list of iterable items (like lists, but not strings). Includes whichever
    of lists, tuples, sets, and Sets are available in this version of Python.
    """
    pass


iters = _hack(iters)


def _strips(direction, text, remove):
    if isinstance(remove, iters):
        for subr in remove:
            text = _strips(direction, text, subr)
        return text

    if direction == "l":
        if text.startswith(remove):
            return text[len(remove):]
    elif direction == "r":
        if text.endswith(remove):
            return text[: -len(remove)]
    else:
        raise ValueError("Direction needs to be r or l.")
    return text


def rstrips(text, remove):
    return _strips("r", text, remove)


def lstrips(text, remove):
    return _strips("l", text, remove)


def strips(text, remove):
    return rstrips(lstrips(text, remove), remove)


def re_subm(pat, repl, string):
    compiled_pat = re_compile(pat)
    proxy = _re_subm_proxy()
    compiled_pat.sub(proxy.__call__, string)
    return compiled_pat.sub(repl, string), proxy.match


def group(seq, size):
    return (seq[i: i + size] for i in range(0, len(seq), size))


def listget(lst, ind, default=None):
    if len(lst) - 1 < ind:
        return default
    return lst[ind]


def intget(integer, default=None):
    try:
        return int(integer)
    except (TypeError, ValueError):
        return default


def dictadd(*dicts):
    result = {}
    for dct in dicts:
        result.update(dct)
    return result


class Memoize:
    def __init__(self, func, expires=None, background=True):
        self.func = func
        self.cache = {}
        self.expires = expires
        self.background = background
        self.running = {}
        self.running_lock = threading.Lock()

    def __call__(self, *args, **keywords):
        key = (args, tuple(keywords.items()))
        with self.running_lock:
            if not self.running.get(key):
                self.running[key] = threading.Lock()

        def update(block=False):
            if self.running[key].acquire(block):
                try:
                    self.cache[key] = (self.func(*args, **keywords), time.time())
                finally:
                    self.running[key].release()

        if key not in self.cache:
            update(block=True)
        elif self.expires and (time.time() - self.cache[key][1]) > self.expires:
            if self.background:
                threading.Thread(target=update).start()
            else:
                update()
        return self.cache[key][0]


memoize = Memoize

re_compile = memoize(re.compile)
re_compile.__doc__ = """
A memoized version of re.compile.
"""


class _re_subm_proxy:
    def __init__(self):
        self.match = None

    def __call__(self, match):
        self.match = match
        return ""
