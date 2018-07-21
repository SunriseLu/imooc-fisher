
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    return 'hello,Sunrise'

app.run(host='0.0.0.0',port=80,debug=app.config['DEBUG'])

