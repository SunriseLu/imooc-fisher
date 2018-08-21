"""
-*- coding: utf-8 -*-
@Time    : 2018/7/27 23:21
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : book.py
"""

from flask import request, flash, render_template
from flask_login import current_user

from app.forms.book import SearchBook
from app.models.gift import Gift
from app.view_models.trade import TradeInfo
from app.models.wish import Wish
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
    has_in_gifts = False
    has_in_wish = False

    book = {}
    if is_isbn(isbn):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        book = BookViewModel(yushu_book.first)
    else:
        flash('isbn不合符要求，请重新输入')

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wish = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_withs = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_viewmodel = TradeInfo(trade_gifts)
    trade_withs_viewmodel = TradeInfo(trade_withs)

    return render_template('book_detail.html', book=book,
                           wishes=trade_withs_viewmodel, gifts=trade_gifts_viewmodel,
                           has_in_wish=has_in_wish, has_in_gifts=has_in_gifts)
