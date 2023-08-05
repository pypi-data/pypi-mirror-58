#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path

# 不能删除
HERE = path.dirname(path.abspath(__file__))

# DEBUG模式
DEBUG = True  # Switch from True to False, you need to restart the app to take effect
# DEBUG输出sql执行情况
DEBUG_SQL = True

# 部署路径 如http://127.0.0.1/test, 则填写"/test"
DEPLOY_PATH = "/"

# 默认编码类型，模板文件输出格式
DEFAULT_CHARSET = "utf-8"
DEF_CONTENT_TYPES = "text/html; charset=utf-8"

# 静态文件路径
STATIC_DIRS = ("/media/", "/static/")

# 数据库配置-可以同时配置多个
DATABASE = {
    'default': {
        "ENGINE": "mssql",  # mssql, mysql, oracle
        "NAME": "testdb",  # database name
        "USER": "sa",  # user
        "PASSWORD": "123456",  # password
        "HOST": "127.0.0.1",  # database host
        "PORT": 1433,  # port
    },
    'mysql': {
        "ENGINE": "mysql",  # mssql, mysql, oracle
        "NAME": "testdb",  # database name
        "USER": "root",  # uid
        "PASSWORD": "123456",  # password
        "HOST": "127.0.0.1",  # database host
        "PORT": 3306,  # port
    }
}

# 模板类型
TEMPLATE_MODEL = "default"  # default, jinja2, mako, genshi
# 模板文件路径
TEMPLATE_DIRS = ("templates", "views")

# SESSION 相关配置
SESSION_COOKIE_NAME = 'LeafPy_session_id'
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_PATH = None
SESSION_COOKIE_TIMEOUT = 86400  # 24 * 60 * 60 -- 24 hours in seconds
SESSION_COOKIE_IGNORE_EXPIRY = True,
SESSION_COOKIE_IGNORE_CHANGE_IP = True,
SESSION_COOKIE_SECRET_KEY = '466e740f065811e49a310021cccc1d0c',
SESSION_COOKIE_EXPIRED_MESSAGE = 'Session expired',
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False

# Session的实现方式
SESSION_STORE = "DiskStore"  # The module to store session data, can use DiskStore, DBStore, RedisStore, ShelfStore
SESSION_STORE_CONFIG = {'path': path.join(HERE, "sessiondir")}  # DiskStore or ShelfStore path for session

"""
#For DiskStore
SESSION_STORE = 'DiskStore'  
SESSION_STORE_CONFIG = {'path': '/tmp'} 

#for DBStore
SESSION_STORE           = 'DBStore'
SESSION_STORE_CONFIG    = { "ENGINE" : "mysql", 
                            "NAME" : "session", 
                            "USER" : "root", 
                            "PASSWORD" : "123456",  
                            "HOST" : "127.0.0.1", 
                            "PORT" : None, 
                            "TABLE_NAME": "session"}

#for RedisStore
SESSION_STORE_CONFIG    = "redis://127.0.0.1:6379/0"
## Redis的配置方法还有如下:
# redis://[:password]@localhost:6379/0
# rediss://[:password]@localhost:6379/0
# unix://[:password]@/path/to/socket.sock?db=0

#for ShelfStore
SESSION_STORE = 'ShelfStore'  
SESSION_STORE_CONFIG = {'path': '/tmp/session.shelf'} 
"""
