#!/usr/bin/env python
# coding:utf-8
from apps.ext import db


class Piao(db.Model):
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=True)
    detail = db.Column(db.String(64), nullable=True)

