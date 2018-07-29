"""
-*- coding: utf-8 -*-
@Time    : 2018/7/28 23:41
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : book.py
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchBook(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
