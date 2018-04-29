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
    ticket = models.Ticket()  #reczne wprowadzenie postĂł do bazy danych
    ticket.nr_trybuny_ticket = "8"
    ticket.user_login = "stara"
    db.session.add(ticket)
    db.session.commit()
    show = models.Concert() #reczne wprowadzenie koncertu
    show.name = "koncert ACDC"
    show.band = "ACDC"
    show.venue = "Spodek"
    show.data = "12.06.2018"
    show.nr_plyta_ticket = 30
    show.price_plyta_ticket = 90
    show.nr_trybuny_ticket = 20
    show.price_trybuny_ticket = 100
    show.nr_gc_ticket = 10
    show.price_gc_ticket = 120
    show.nr_vip_ticket = 5
    show.price_vip_ticket = 140
    show.opis = "Koncert jednego z najstarszych zespołów"
    db.session.add(show)
    db.session.commit()



if __name__ == '__main__':
    db_start()
