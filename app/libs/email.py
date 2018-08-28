"""
-*- coding: utf-8 -*-
@Time    : 2018/8/27 22:19
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : email.py
"""
from flask import current_app, render_template

from app import email
from flask_mail import Message


def send_message(to, subject, template_name_or_list, **kwargs):
    # msg = Message('测试邮件', sender='sa5122772@163.com',
    #               body='Test', recipients=['sa5122772@163.com'])
    msg = Message('【鱼书】' + '' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template_name_or_list, **kwargs)
    email.send(msg)
