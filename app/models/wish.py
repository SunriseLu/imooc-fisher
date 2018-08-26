"""
-*- coding: utf-8 -*-
@Time    : 2018/8/13 23:38
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : gift.py
"""
from flask import current_app
from flask_login import current_user
from sqlalchemy import Integer, Column, Boolean, ForeignKey, String, desc
from sqlalchemy.orm import relationship

from app.libs.helper import is_isbn
from app.models.base import Base

from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False, unique=True)


    def can_save_to_list(self, isbn):
        from app.models.gift import Gift
        if not isbn or not is_isbn(isbn):
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        user = current_user
        gift_list = Gift.query.filter_by(isbn=isbn, uid=user.id, launched=False).first()
        wish_list = Wish.query.filter_by(isbn=isbn, uid=user.id, launched=False).first()
        if not gift_list and not wish_list:
            return True
        return False

    @classmethod
    def recent_gifts(cls):
        recent = Wish.query.filter_by(
            launched=False).order_by(
            desc(Wish.create_time)).group_by(
            Wish.isbn).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first