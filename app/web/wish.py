from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app import db
from app.models.user import User
from app.models.wish import Wish
from app.view_models.gift import MyGifts
from app.view_models.wish import MyWishs
from . import web

__author__ = '七月'


def limit_key_prefix():
    pass


@web.route('/my/wish')
@login_required
def my_wish():
    user = User.query.get(current_user.id)
    view_model = MyWishs(user.wishs) #wish跟gift一样。所有使用一样的viewmode
    print(user.wishs[0].book)
    return render_template('my_gifts.html', gifts=view_model.my_gifts) #my_wish页面出现问题。用gift也代替


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
