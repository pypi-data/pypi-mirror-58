#!/usr/bin/env python
# -*- coding: utf-8 -*-

import LeafPy

app = LeafPy.application(globals())

application = app.wsgifunc()

# 如果使用spawn-fcgi方式运行，必须将以下一行代码取消注释
# LeafPy.wsgi.runwsgi = lambda func, addr=None: LeafPy.wsgi.runfcgi(func, addr)

if __name__ == "__main__":
    app.run()
