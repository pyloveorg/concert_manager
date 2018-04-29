__author__ = 'Piotr Dyba, Krzysztof Michalak'

from sqlalchemy import Column, DateTime
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.types import Boolean

from main import db, bcrypt


class User(db.Model):
    """
    User model for reviewers.
    """
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(20), unique=True)
    active = Column(Boolean, default=True)
    email = Column(String(30), unique=True)
    hashed_password = Column(String(20))
    usertype = Column(String(15), default="organizer")
    about = Column(String(200), default="")
    admin = Column(Boolean, default=False)
    is_anonymous = False
    is_authenticated = True
    posts = db.relationship('Ticket', backref='buyer', lazy='dynamic')
    
    def get_id(self):
        return str(self.id)

    def get(self):
        return self

    def is_active(self):
        """
        Returns if user is active.
        """
        return self.active

    def is_admin(self):
        """
        Returns if user is admin.
        """
        return self.admin

    def set_password(self, password):
        self.hashed_password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.hashed_password, password)


class Ticket(db.Model):
    __tablename__ = 'ticket'
    ticket_id = Column(Integer, autoincrement=True, primary_key=True)
    user_login = db.Column(db.String(20), db.ForeignKey('user.username'))
    nr_plyta_ticket = db.Column(Integer)
    price_plyta_ticket = db.Column(db.Float)
    nr_trybuny_ticket = db.Column(Integer)
    price_trybuny_ticket = db.Column(db.Float)
    nr_gc_ticket = db.Column(Integer)
    price_gc_ticket = db.Column(db.Float)
    nr_vip_ticket = db.Column(Integer)
    price_vip_ticket = db.Column(db.Float)
    show_id = db.Column(Integer)
    band = db.Column(db.String(30))

    def get(self):
        return str(self)


class Concert(db.Model):
    __tablename__ = 'concert'
    id = Column(Integer, autoincrement=True, primary_key=True)
    band = db.Column(String(30))
    name = db.Column(db.String(100))
    opis = db.Column(String(200), default="")
    gatunek = db.Column(String(20))
    price_plyta_ticket = db.Column(db.Float)
    price_trybuny_ticket = db.Column(db.Float)
    price_gc_ticket = db.Column(db.Float)
    price_vip_ticket = db.Column(db.Float)
    nr_plyta_ticket = db.Column(Integer)
    nr_trybuny_ticket = db.Column(Integer)
    nr_gc_ticket = db.Column(Integer)
    nr_vip_ticket = db.Column(Integer)
    data = db.Column(db.String(20))
    venue = db.Column(String(30))

    def get(self):
        return str(self)
