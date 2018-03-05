__author__ = 'Piotr Dyba, Krzysztof Michalak'

from os import path, urandom

from flask import Flask, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = urandom(24)
db = SQLAlchemy()
db.app = app
db.init_app(app)
loginManager = LoginManager()
loginManager.init_app(app)
bcrypt = Bcrypt()
app.static_path = path.join(path.abspath(__file__), 'static')


if __name__ == '__main__':
    from views import *
    app.run(debug=True)
