"""
-*- coding: utf-8 -*-
@Time    : 2018/7/23 22:21
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : helper.py
"""


def is_isbn_or_key(word):
    """
    判断关键字的类型
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key


def is_isbn(isbn):
    if isbn:
        return True if is_isbn_or_key(isbn) == 'isbn' else False
    else:
        return False
