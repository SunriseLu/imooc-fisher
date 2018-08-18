from flask import flash, render_template, current_app

from app.libs.helper import is_isbn
from app.models import Gift, Wish, db
from app.spider.yushu_book import YuShuBook
from . import web
from flask_login import login_required, current_user

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'hello gifts'


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
        try:
            gift.isbn = isbn
            gift.uid = user.id
            user.beans += current_app.config['ADD_BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    else:
        flash('这本书已经添加到你的赠送清单或心愿清单中，请不要重复添加')
    return 'ok'


@web.route('/gifts/<gid>/redraw')
# @login_required
def redraw_from_gifts(gid):
    pass
