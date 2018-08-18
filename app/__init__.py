"""
-*- coding: utf-8 -*-
@Time    : 2018/7/27 23:23
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : __init__.py
"""
from flask import Flask
# from app.models.book import db
from app.models import db
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_bluepriter(app)

    login_manager.init_app(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_bluepriter(app):
    from app.web.book import web
    app.register_blueprint(web)
