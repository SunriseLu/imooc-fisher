from flask import render_template

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web

__author__ = '七月'


@web.route('/')
def index():
    # 最近上传的礼物列表
    recent_gifts = [BookViewModel(gift.book) for gift in Gift.recent_gifts()]
    return render_template('index.html', recent=recent_gifts)


@web.route('/personal')
# @login_required
def personal_center():
    pass
