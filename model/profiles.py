from datetime import date
import os, base64
import json, hashlib, binascii
from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class Profile(db.Model):
    __tablename__ = 'profiles'
    _username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    _email = db.Column(db.String(120), unique=True, nullable=False)
    _high_score = db.Column(db.Integer(500), unique=False, nullable=False)
    _starred_games = db.Column(db.Integer(100), unique=True, nullable=False)
    _points_per_second = db.Column(db.Integer(100), unique=False, nullable=False)

    def __init__(self, username, email, high_score, starred_games, points_per_second):
        self._username = username
        self._email = email
        self._high_score = high_score
        self._starred_games = starred_games
        self._points_per_second = points_per_second


    #Setter and getter functions

    # username getter and setter functions
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    # email getter and setter functions
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    # high score getter and setter functions
    @property
    def high_score(self):
        return self._high_score

    @high_score.setter
    def high_score(self, high_score):
        if high_score > self._high_score:
            self._high_score = high_score

    # starred games getter and setter functions
    # not yet sure how this data will be stored, but I'm creating the getter and setter of some string called _starred_games now
    @property
    def starred_games(self):
        return self._starred_games
    
    @starred_games.setter
    def starred_games(self, starred_games):
        self._starred_games = starred_games

    # points per second getter and setter functions

    @property
    def points_per_second(self):
        return self._points_per_second
    
    @points_per_second.setter
    def points_per_second(self, points_per_second):
        self._points_per_second = points_per_second

    

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        return {'username': self._username, 'email': self._email, 'high_score': self._high_score, 'points_per_second': self._points_per_second}

    def update(self, username, email, high_score, points_per_second):
        self._username = username
        self._email = email
        if high_score > self._high_score:
            self._high_score = high_score
        self._points_per_second = points_per_second
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None