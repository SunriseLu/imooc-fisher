"""
-*- coding: utf-8 -*-
@Time    : 2018/8/21 23:04
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : trade.py
"""


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__single(o) for o in goods]

    def __single(self, good):
        if good.create_datetime:
            time = good.create_datetime.strftime("%Y-%M-%D")
        else:
            time = '未知'
        return {
            'user_name': good.user.nickname,
            'id': good.id,
            'time': time
        }
