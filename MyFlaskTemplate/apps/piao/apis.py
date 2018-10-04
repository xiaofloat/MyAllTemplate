#!/usr/bin/env python
# coding:utf-8
from flask import session
from flask_restful import Resource


class PiaoApi(Resource):
    def get(self):
        result = session.get('name')
        return result
