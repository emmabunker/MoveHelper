""" code modified from https://kanchanardj.medium.com/how-to-add-data-from-flask-to-postgresql-in-windows-2-77af756d017f """

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True

def __init__(self, *args):
        super().__init__(*args)

def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

class User(db.Model):
    __tablename__ = 'user'
    firstname = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email