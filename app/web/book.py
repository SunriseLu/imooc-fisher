"""
-*- coding: utf-8 -*-
@Time    : 2018/7/27 23:21
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : book.py
"""
from flask import jsonify, request

from app.forms.book import SearchBook
from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search')
def seacrh():
    """
    :param q:关键字
    :param page: 显示页数
    :return:
    """

    form = SearchBook(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'key':
            result = YuShuBook.search_by_keyword(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        return jsonify(result)
    else:
        return jsonify({'msg': '参数错误'})
