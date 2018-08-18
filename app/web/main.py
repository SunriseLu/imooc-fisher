from . import web


__author__ = '七月'


@web.route('/')
def index():
    return 'index'

@web.route('/personal')
# @login_required
def personal_center():
    pass