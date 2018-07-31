"""
-*- coding: utf-8 -*-
@Time    : 2018/7/23 22:58
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : yushu_book.py
"""
import myhttp


class YuShuBook:
    # isbn_url = 'http://t.yushu.im/v2/isbn/{}'
    # keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = myhttp.HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        result = myhttp.HTTP.get(cls.keyword_url.format(keyword, count, start))
        return result
