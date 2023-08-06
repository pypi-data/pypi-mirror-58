#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from LeafPy import autodelegate
from LeafPy import http
# from LeafPy.db import sql as dbn
from LeafPy.conf import settings


class Index:
    # @http.jsonresult
    def GET(self):
        req = http.input(status=1)

        """default dbn useage"""
        # ret = dbn.select("select top 10 * from paper_order", status=req.status)
        # print(len(ret[1].list()))
        """other dbn useage"""
        # ret = dbn.mysql.select("select * from mzitu_class")
        # print(len(ret[1].list()))
        # z = ret[1].list()
        # return z #直接输出json需要在Method方法前面开启http.jsonresult解释器

        """db Transaction demo"""
        # with dbn.transaction() as tx:
        #    tx.insert("test", name="1")
        #    tx.update("test", "name=?", "2", status=0)
        #    # 下面是错误的 sql 语句，有错误，则上面的 sql 语句不会成功执行。
        #    tx.insert('abc')

        """set session"""
        # http.session["dbresult"] = z

        # return http.render.mako(word="Hello World! Mako", rds=z)

        # return http.render.jinja(word="Hello World! Jinja2", rds=z)

        # return ("text/plaint;charset=utf-8", "hello world!!!!")

        # return http.TemplateResponse("hello.html", name="Hello World! LeafPy.", city="杭州", escape=True)

        # http.seeother('./test')

        return http.render.hello(name="yhq", method="Default Get")


class Test:
    def GET(self, *args):
        """ session get """
        dbresult = http.session.get("dbresult")
        print(dbresult)
        print("args: {}".format(args))
        return ("text/plaint;charset=utf-8", "test session value is: {}".format(dbresult))


class Upload:  # to upload file
    def GET(self):
        req = http.input(message="")
        message = req.message or ""
        return http.render.upload(message=message)

    @http.jsonresult
    def POST(self):
        req = http.input(myfile={})
        savepath = os.path.join(settings.HERE, "upload")
        if not os.path.exists(savepath):
            os.makedirs(savepath)
        if 'myfile' in req:
            filepath = req.myfile.filename.replace('\\', '/')
            filename = filepath.split('/')[-1]
            if not filename:
                return dict(retcode=0, msg="please chooise a file to upload")

            savefile = os.path.join(savepath, filename)
            with open(savefile, "wb") as f:
                f.write(req.myfile.file.read())

        return dict(retcode=1, msg="ok")


class Task:  # Delegate Method test
    GET = autodelegate("GET_")

    def GET_sync(self):
        return http.render.hello(name='yhq', method='sync')

    def GET_send(self):
        return http.render.hello(name='yhq', method='send')

    def GET_(self):
        return http.render.hello(name='yhq', method='Empty')
