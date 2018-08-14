"""
-*- coding: utf-8 -*-
@Time    : 2018/7/30 23:35
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : __init__.py.py
"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from app.models.book import Book
from app.models.gift import Gift
from app.models.user import User
from app.models.base import Base
