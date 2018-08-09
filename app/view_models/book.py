"""
-*- coding: utf-8 -*-
@Time    : 2018/8/7 22:53
@Author  : Sunrise.Lu
@Email   : jie.yxy@gmail.com
@File    : book.py
"""


class BookViewModel:
    def __init__(self, data):
        self.title = data['title']
        self.publisher = data['publisher']
        self.pages = data['pages'] or ''
        self.author = '&'.join(data['author'])
        self.price = data['price']
        self.summary = data['summary'] or ''
        self.image = data['image']

class BookCollectionViewModel:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword

class _BookViewModel:
    data_template = {
        'books': [],
        'total': 0,
        'keyword': ''
    }

    @classmethod
    def package_single(cls, data, keyword):
        returned = cls.data_template
        returned['keyword']: keyword
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_detail(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = cls.data_template
        returned['keyword']: keyword
        if data:
            returned['total']: data['total']
            returned['books']: [cls.__cut_detail(book) for book in data['books']]
            # 列表推导式
        return returned

    @staticmethod
    def __cut_detail(data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',  # 比三元还好用，简单null转为空字符
            'author': '、'.join(data['author']),  # 把列表每一项用顿号连接
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
