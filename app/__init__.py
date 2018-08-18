"""
-*- coding: utf-8 -*-
@Time    : 2018/7/27 23:23
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : __init__.py
"""
from flask import Flask
# from app.models.book import db
from app.models.base import db
from app.spider._flask_login import login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_bluepriter(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或者注册'

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_bluepriter(app):
    from app.web.book import web
    app.register_blueprint(web)
