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

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = myhttp.HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page):
        result = myhttp.HTTP.get(self.keyword_url.format(keyword, current_app.config['PER_PAGE'],
                                                         self.calculate_start(page)))
        self.__fill_collection(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
