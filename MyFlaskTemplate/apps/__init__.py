#!/usr/bin/env python
# coding:utf-8
from flask import Flask
from flask_cors import CORS
from apps.ext import init_db, init_cache, init_session
from apps.urls import init_api, init_blue

# 实例化flask核心对象
app = Flask(__name__)
app.debug = True

# 解决跨域请求问题
CORS(app=app, supports_credengtials=True)


# 注册蓝图
def register_blue():
    init_blue(app)


# 注册数据库
def register_db():
    init_db(app)


# 注册缓存
def register_cache():
    init_cache(app)


# 注册restful的api
def register_api():
    init_api(app)

# 注册session配置
def register_session():
    init_session(app)


# 加工创建app
def create_app():
    register_blue()
    register_db()
    register_api()
    register_cache()
    register_session()
    return app
