#!/usr/bin/env python
# -*- coding: utf-8 -*-

from LeafPy import http
from LeafPy.utils import imgcode


class ImgCode:
    def GET(self):
        c = imgcode.picChecker(foregroundColor=(0, 0, 255),
                               outputType="png",
                               length=5,
                               size=(120, 27), useFormula=True)
        code, imgdata = c.out()
        http.session['rndcode'] = code
        return http.render.imgcode(imgdata=imgdata)
