#!/usr/bin/env python
# coding:utf-8
from flask_restful import Api

# 实例化api对象
from apps.piao.apis import PiaoApi
from apps.piao.views import piao_blue

api = Api()
# 添加源
api.add_resource(PiaoApi, '/piao/2')


# 初始化api
def init_api(app):
    api.init_app(app)


# 蓝图
def init_blue(app):
    app.register_blueprint(piao_blue)
