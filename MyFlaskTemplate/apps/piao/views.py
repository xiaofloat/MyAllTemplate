#!/usr/bin/env python
# coding:utf-8
from flask import Blueprint, session, render_template

from apps.ext import cache
from apps.piao.models import Piao

piao_blue = Blueprint('piao', __name__)


@piao_blue.route('/piao/')
@cache.cached(key_prefix='xiaogege')
def piao():
    session['name'] = 'piao'
    return 'piao'


@piao_blue.route('/')
def index():
    return render_template('index.html')
