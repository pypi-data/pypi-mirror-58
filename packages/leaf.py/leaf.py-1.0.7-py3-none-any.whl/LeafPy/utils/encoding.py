#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .py3helpers import (
    PY2,
    is_iter,
    text_type,
    imap,
)


def safeunicode(obj, encoding="utf-8"):
    t = type(obj)
    if t is text_type:
        return obj
    elif t is bytes:
        return obj.decode(encoding)
    elif t in [int, float, bool]:
        return text_type(obj)
    else:
        return text_type(obj)


def safestr(obj, encoding="utf-8"):
    if PY2 and isinstance(obj, text_type):
        return obj.encode(encoding)
    elif is_iter(obj):
        return imap(safestr, obj)
    else:
        return str(obj)


if not PY2:
    # Since Python3, utf-8 encoded strings and unicode strings are the same thing
    safeunicode = safestr


def uni2hex(c):
    hexchr = hex(ord(c))
    hexchr = "&#%s;" % hexchr[1:]
    return hexchr


def hex2uni(c):
    hexchr = "0%s" % c[2:-1]
    try:
        uchr = chr(eval(hexchr))
    except:
        return u'Er!'
    return uchr


def str2hex(s, slen=0):
    us = safeunicode(s)

    if slen > 0 and len(us) > slen:
        us = us[:slen - 3] + u'...'

    h = list()
    for c in us:
        h.append(uni2hex(c))

    hstr = "".join(h)
    if hstr.startswith('&#xa;'):
        hstr = hstr[5:]
    return hstr.replace('&#xa;', '\n')


def safe_utf8chinese(s, slen=0):
    us = safeunicode(s)
    if slen > 0 and len(us) > slen:
        us = us[:slen - 3] + u'...'

    h = list()
    try:
        h.append(us.encode('utf-8'))
    except:
        for c in us:
            if ischinese(c):
                h.append(uni2hex(c))
            else:
                h.append(c.encode('utf-8'))
    return "".join(h)


def ischinese(s):
    try:
        scode = ord(s)
        if scode >= 0x4E00 and scode <= 0x9FBF: return True
    except:
        pass

    return False


safeutf8 = safe_utf8chinese
