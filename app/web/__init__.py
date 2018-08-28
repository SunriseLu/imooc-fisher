"""
-*- coding: utf-8 -*-
@Time    : 2018/7/27 23:52
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : __init__.py
"""
from flask import Blueprint

web = Blueprint('web', __name__)

@web.app_errorhandler(404)
def not_found(error):
    return '页面不存在'


from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish