"""
-*- coding: utf-8 -*-
@Time    : 2018/8/13 23:38
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : gift.py
"""

from sqlalchemy import Integer, Column, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from . import db


class Gift(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False, unique=True)
