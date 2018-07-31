"""
-*- coding: utf-8 -*-
@Time    : 2018/7/23 22:58
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : yushu_book.py
"""
from app.libs import myhttp
from flask import current_app


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = myhttp.HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page):
        result = myhttp.HTTP.get(cls.keyword_url.format(keyword, current_app.config['PER_PAGE'],
                                                        cls.calculate_start(page)))
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
