"""
-*- coding: utf-8 -*-
@Time    : 2018/8/25 23:39
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : gift.py
"""
from collections import namedtuple

from app.view_models.book import BookViewModel

MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyGifts():

    def __init__(self, current_gifts):
        self.my_gifts = []
        self.__current_gifts = current_gifts

        self.my_gifts = self.__fill()

    def __fill(self):
        temp_gifts = []
        for gift in self.__current_gifts:
            my_gift = MyGift(gift.id, BookViewModel(gift.book), gift.wish_count)
            temp_gifts.append(my_gift)
        return temp_gifts
