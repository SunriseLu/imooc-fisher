
from . import web


__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    pass


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


# 单元测试
@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
@login_required
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
