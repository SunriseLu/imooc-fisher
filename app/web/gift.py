import json

from flask import flash, current_app, redirect, url_for, render_template

from app.models.gift import Gift

from app.models.base import db
from app.models.user import User
from app.view_models.book import BookViewModel
from app.view_models.gift import MyGifts

from . import web
from flask_login import login_required, current_user

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    user = User.query.get(current_user.id)
    view_model = MyGifts(user.gifts)

    return render_template('my_gifts.html', gifts = view_model.my_gifts)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    # 判断isbn是否为空和是否为isbn
    # 判断isbn对应的书是否存在
    # 判断用户的书是否有同样的书在赠送列表中
    # 判断用户的书是否在愿望清单中

    gift = Gift()
    user = current_user
    if gift.can_save_to_list(isbn):
        with db.auto_commit():
            gift.isbn = isbn
            gift.uid = user.id
            user.beans += current_app.config['ADD_BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()

    else:
        flash('这本书已经添加到你的赠送清单或心愿清单中，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
# @login_required
def redraw_from_gifts(gid):
    pass
