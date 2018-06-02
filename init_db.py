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
    user.usertype = "admin"
    db.session.add(user)
    db.session.commit()
    show = models.Concert() #reczne wprowadzenie koncertu
    show.name = "koncert ACDC"
    show.band = "ACDC"
    show.venue = "Spodek"
    show.nr_plyta_ticket = 30
    show.price_plyta_ticket = 90
    show.nr_trybuny_ticket = 20
    show.price_trybuny_ticket = 100
    show.nr_gc_ticket = 10
    show.price_gc_ticket = 120
    show.nr_vip_ticket = 5
    show.price_vip_ticket = 140
    show.opis = "Koncert jednego z najstarszych zespołów"
    show.data = "2018, 6, 5"
    show.godzina = "20:00"
    show.venue = "Zamek"
    show.picurl = "http://www.cdn.ug.edu.pl/wp-content/uploads/2017/01/koncert.jpg"
    db.session.add(show)
    db.session.commit()



if __name__ == '__main__':
    db_start()
