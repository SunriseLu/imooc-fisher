"""
-*- coding: utf-8 -*-
@Time    : 2018/8/14 14:25
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : base.py
"""
from sqlalchemy import Column, Integer, SmallInteger

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
