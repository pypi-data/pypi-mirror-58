#!/usr/bin/env python
# -*- coding: utf-8 -*-
HERE = "/"

# DEBUG模式
DEBUG = True
# DEBUG输出sql执行情况
DEBUG_SQL = True

# 部署路径 如http://127.0.0.1/test, 则填写"/test"
DEPLOY_PATH = "/"

# 默认编码类型，模板文件输出格式
DEFAULT_CHARSET = "utf-8"
DEF_CONTENT_TYPES = "text/html; charset=utf-8"

# 默认静态文件路径
STATIC_PATH = ("/static/", "/meida/", "/favicon.ico", "/robots.txt")
# 可配置静态文件路径
STATIC_DIRS = ()

# 模板类型
TEMPLATE_MODEL = "default"  # default, jinja2, mako, genshi
# 默认模板文件路径
TEMPLATE_PATH = ('templates',)
# 可配置模板文件路径
TEMPLATE_DIRS = ()

# 数据库配置-可以同时配置多个
DATABASE = {"default": {}, }

# SESSION 相关配置
SESSION_COOKIE_NAME = 'LeafPy_session_id'
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_PATH = None
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_TIMEOUT = 8 * 60 * 60  # timeout for session (seconds)
SESSION_COOKIE_IGNORE_EXPIRY = True,
SESSION_COOKIE_IGNORE_CHANGE_IP = True,
SESSION_COOKIE_SECRET_KEY = '9a515b80e7ca11e3a626',
SESSION_COOKIE_EXPIRED_MESSAGE = 'Session expired',

SESSION_STORE = None  # The module to store session data, can use DiskStore, DBStore, RedisStore, ShelfStore
SESSION_STORE_CONFIG = {}  # DiskStore or ShelfStore path for session
"""
#For DiskStore
SESSION_STORE = 'DiskStore'  
SESSION_STORE_CONFIG = {'path': '/tmp'} 

#for DBStore
SESSION_STORE           = 'DBStore'
SESSION_STORE_CONFIG    = { "ENGINE" : "mysql", 
                            "NAME" : "session", 
                            "USER" : "root", 
                            "PASSWORD"  : "123456",  
                            "HOST" : "127.0.0.1", 
                            "PORT" : None, 
                            "TABLE_NAME": "session"}

#for RedisStore
SESSION_STORE_CONFIG    = "redis://[:password]@[host]:[port]/[db_index]"

## Redis的配置方法还有如下:
# redis://[:password]@localhost:6379/0
# rediss://[:password]@localhost:6379/0
# unix://[:password]@/path/to/socket.sock?db=0
                            
#for ShelfStore
SESSION_STORE = 'ShelfStore'  
SESSION_STORE_CONFIG = {'path': '/tmp/session.shelf'} 
"""
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False
