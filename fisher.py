from flask import Flask, jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    return 'hello,Sunrise'


@app.route('/book/search/<q>/<page>')
def seacrh(q, page):
    """
    :param q:关键字
    :param page: 显示页数
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'key':
        result = YuShuBook.search_by_keyword(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    return jsonify(result)


app.run(host='0.0.0.0', port=80, debug=app.config['DEBUG'])
