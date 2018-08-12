from . import web

__author__ = '七月'


@web.route('/set/cookie')
def set_cookie():
    pass

@web.route('/set/session')
def set_session():
    pass

@web.route('/get/session')
def get_session():
    pass
