#!/usr/bin/env python
# -*- coding: utf-8 -*-

urlpatterns = {
    '/imgcode': 'index.rndcode.ImgCode',

    '/': 'index.actions.Index',
    '/upload': 'index.actions.Upload',
    '/test/(.*)': 'index.actions.Test',
    '/task_(.*)': 'index.actions.Task',
}
