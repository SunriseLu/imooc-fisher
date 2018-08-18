# imooc-fisher
imooc的python课程练习

#install
1.pipenv install flask
2.pipenv install requests
3.pipenv install wtforms
4.pipenv install flask-sqlalchemy
5.pipenv install cymysql
6.pipenv install flask-login




#new python file secure.py /app
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://fisher:fisher@192.168.199.122:3307/fisher'
SECRET_KEY = '123'