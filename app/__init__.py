"""
-*- coding: utf-8 -*-
@Time    : 2018/7/27 23:23
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : __init__.py
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_bluepriter(app)
    return app


def register_bluepriter(app):
    from app.web.book import web
    app.register_blueprint(web)
