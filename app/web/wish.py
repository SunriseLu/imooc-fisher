from . import web

__author__ = '七月'


def limit_key_prefix():
    pass


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
# @login_required
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
@limiter.limit(key_func=limit_key_prefix)
# @login_required
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
# @login_required
def redraw_from_wish(isbn):
    pass


@limiter.limited
def satifiy_with_limited():
    pass
