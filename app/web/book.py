"""
-*- coding: utf-8 -*-
@Time    : 2018/7/27 23:21
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : book.py
"""
from flask import jsonify, Blueprint
from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook



@web.route('/book/search/<q>/<page>')
def seacrh(q, page):
    """
    :param q:关键字
    :param page: 显示页数
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'key':
        result = YuShuBook.search_by_keyword(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    return jsonify(result)
