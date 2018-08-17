"""
-*- coding: utf-8 -*-
@Time    : 2018/8/13 23:38
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : user.py
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash

from . import db
from app.models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(128))
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    Wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
