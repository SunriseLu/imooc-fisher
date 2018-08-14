"""
-*- coding: utf-8 -*-
@Time    : 2018/8/14 14:25
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : base.py
"""
from sqlalchemy import Column, Integer, SmallInteger

from . import db


class Base(db.Model):
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)
