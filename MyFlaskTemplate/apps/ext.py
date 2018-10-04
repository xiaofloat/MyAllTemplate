#!/usr/bin/env python
# coding:utf-8
import os

import redis
from flask_caching import Cache
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

# 初始化数据库操作对象
db = SQLAlchemy()
# 初始化数据库迁移对象
migrate = Migrate()
# 数据库的配置
DB_SETTING = {
    'ENGIN': 'mysql',
    'DRIVER': 'pymysql',
    'USER': 'root',
    'PASSOWRD': '1995',
    'HOST': '139.199.164.245',
    'PORT': 3306,
    'DATABASE': 'my_flask'
}


# 获得数据库的uri
def get_db_uri():
    return '{}+{}://{}:{}@{}:{}/{}'.format(
        DB_SETTING['ENGIN'],
        DB_SETTING['DRIVER'],
        DB_SETTING['USER'],
        DB_SETTING['PASSOWRD'],
        DB_SETTING['HOST'],
        DB_SETTING['PORT'],
        DB_SETTING['DATABASE']
    )


# 初始化数据库
def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    migrate.init_app(app, db)


# 实例化缓存对象
cache = Cache()


# 初始化缓存
def init_cache(app):
    # 缓存的配置
    config = {
        # 缓存的过期时间，单位：秒
        'CACHE_DEFAULT_TIMEOUT': 60,
        # 缓存的类型
        'CACHE_TYPE': 'redis',
        # host
        'CACHE_REDIS_HOST': '139.199.164.245',
        # 端口
        'CACHE_REDIS_PORT': '6379',
        # 密码
        'CACHE_REDIS_PASSWORD': '1995',
        # 选择redis的哪个数据库
        'CACHE_REDIS_DB': 0,
        # 缓存key的前缀
        'CACHE_KEY_PREFIX': 'piao_'
    }
    cache.init_app(app, config)


# 实例化session配置对象
session = Session()


# 初始化session配置
def init_session(app):
    # 设置session密匙
    app.config['SECRET_KEY'] = os.urandom(24)  # 随机产生24位的字符串作为SECRET_KEY
    # session类型为redis
    app.config['SESSION_TYPE'] = 'redis'
    # 如果设置为True，则关闭浏览器session就失效。
    app.config['SESSION_PERMANENT'] = False
    # 是否对发送到浏览器上session的cookie值进行加密
    app.config['SESSION_USE_SIGNER'] = False
    # 保存到session中的值的前缀
    app.config['SESSION_KEY_PREFIX'] = 'session:'
    # session过期时间
    app.config['PERMANENT_SESSION_LIFETIME'] = 60*60
    # 用于连接redis的配置
    app.config['SESSION_REDIS'] = redis.Redis(host='139.199.164.245', port='6379', password='1995')
    session.init_app(app)
