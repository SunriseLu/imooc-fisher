from flask import flash, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.models.wish import Wish
from . import web

__author__ = '七月'


def limit_key_prefix():
    pass


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    wish = Wish()
    user = current_user
    if wish.can_save_to_list(isbn):
        with db.auto_commit():
            wish.isbn = isbn
            wish.uid = user.id
            db.session.add(wish)
            db.session.commit()

    else:
        flash('这本书已经添加到你的赠送清单或心愿清单中，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))




@web.route('/satisfy/wish/<int:wid>')
# @limiter.limit(key_func=limit_key_prefix)
# @login_required
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
# @login_required
def redraw_from_wish(isbn):
    pass


# @limiter.limited
def satifiy_with_limited():
    pass
