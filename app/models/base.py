"""
-*- coding: utf-8 -*-
@Time    : 2018/8/14 14:25
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : base.py
"""
from datetime import datetime

from sqlalchemy import Column, Integer, SmallInteger

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
