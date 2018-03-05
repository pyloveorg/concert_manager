__author__ = 'Piotr Dyba, Krzysztof Michalak'

from sqlalchemy import Column
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
