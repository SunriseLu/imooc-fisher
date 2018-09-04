from flask import render_template, flash, url_for, redirect
from flask_login import login_required, current_user

from app.models.gift import Gift
from app.models.user import User
from . import web

__author__ = '七月'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)
    if not current_gift and current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的')
        redirect(url_for('web.book_detail', isbn=current_gift.isbn))


    if not current_user.can_send_gift():
        return render_template('not_enough_beans.html', beans=current_user.beans)

    gifter = current_gift.user.summary
    return render_template('drift.html', gifter=gifter, userbeans=current_user.beans)


@web.route('/pending')
@login_required
def pending():
    #1.在礼物清单和心愿清单中寻找当前用户id 的记录
    #2.上面的记录判断自己的角色并添加项 you_are :requester /gifter
    #3.判断记录的状态 status_str
    #4.渲染模板
    pass



@web.route('/drift/<int:did>/reject')
# @login_required
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
# @login_required
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
# @login_required
def mailed_drift(did):
    pass


def save_drift(drift_form, current_gift):
    pass
