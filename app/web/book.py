"""
-*- coding: utf-8 -*-
@Time    : 2018/7/27 23:21
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : book.py
"""
import json

from flask import jsonify, request, flash, render_template

from app.forms.book import SearchBook, SearchByISBN
from app.view_models.book import BookViewModel, BookCollectionViewModel
from . import web
from app.libs.helper import is_isbn_or_key, is_isbn
from app.spider.yushu_book import YuShuBook


@web.route('/book/search')
def search():
    """
    :param q:关键字
    :param page: 显示页数
    :return:
    """

    form = SearchBook(request.args)
    books = BookCollectionViewModel()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            books.fill(yushu_book, q)
        if isbn_or_key == 'key':
            yushu_book.search_by_keyword(q, page)
            books.fill(yushu_book, q)

        # return json.dumps(books, default=lambda o: o.__dict__)

    else:
        # return jsonify({'msg': '参数错误'})
        flash('搜索条件不符合要求，请重新输入')
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    book = {}
    if is_isbn(isbn):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        book = BookViewModel(yushu_book.first)
    else:
        flash('isbn不合符要求，请重新输入')
    return render_template('book_detail.html', book=book, wishes={}, gifts={})
