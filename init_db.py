__author__ = 'Piotr Dyba, Krzysztof Michalak'

from sqlalchemy import create_engine
from main import db
import models


def db_start():
    create_engine('sqlite:///tmp/test.db', convert_unicode=True)
    db.create_all()
    db.session.commit()
    user = models.User()
    user.set_password('123')
    user.username = 'admin'
    user.email = 'admin@strona.pl'
    user.admin = True
    db.session.add(user)
    db.session.commit()



if __name__ == '__main__':
    db_start()
