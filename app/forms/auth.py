"""
-*- coding: utf-8 -*-
@Time    : 2018/8/17 14:54
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : auth.py
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮件不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])

    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='呢称至少需要两个字符，最多十个字符')])
