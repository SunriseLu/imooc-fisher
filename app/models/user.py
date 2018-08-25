"""
-*- coding: utf-8 -*-
@Time    : 2018/8/13 23:38
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : user.py
"""
from sqlalchemy import Column, Integer, String, Boolean, Float, func, desc
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import Base, db

from flask_login import UserMixin

from app.models.gift import Gift
from app.models.wish import Wish
from app.spider._flask_login import login_manager


class User(UserMixin, Base):
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

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    @property
    def gifts(self):
        gifts = Gift.query.filter_by(uid=self.id, launched=False) \
            .order_by(desc(Gift.create_time)).all()
        isbn_list = [gift.isbn for gift in gifts]
        wish_count_list = self.__get_wish_count(isbn_list)
        for gift in gifts:
            gift.wish_count = self.__search_in_wish_count_list(
                gift.isbn, wish_count_list)
        return gifts

    def __get_wish_count(self, isbn_list):
        count_list = db.session.query(func.count(Wish.id), Wish.isbn) \
            .filter(Wish.launched == False,
                    Wish.isbn.in_(isbn_list),
                    Wish.status == 1) \
            .group_by(Wish.isbn).all()
        return [{'count': w[0], 'isbn': w[1]} for w in count_list]

    def __search_in_wish_count_list(self, isbn, _list):
        count = 0
        for single in _list:
            if isbn == single['isbn']:
                count = single['count']
        return count

    @login_manager.user_loader
    def get_user(uid):
        return User.query.get(int(uid))
