from . import web

__author__ = '七月'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
# @login_required
def send_drift(gid):
    pass


@web.route('/pending')
# @login_required
def pending():
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
