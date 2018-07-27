from flask import Flask, jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook

import app

app = app.create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=app.config['DEBUG'])
