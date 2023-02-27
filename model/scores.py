from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Scores(db.Model):
    __tablename__ = 'score' 
   
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    _username = db.Column(db.String(255))
    _score1 = db.Column(db.Integer, unique=False, nullable=False)
    _score2 = db.Column(db.Integer, unique=False, nullable=False)
    _score3 = db.Column(db.Integer, unique=False, nullable=False)
    _score4 = db.Column(db.Integer, unique=False, nullable=False)
    _score5 = db.Column(db.Integer, unique=False, nullable=False)
    _score6 = db.Column(db.Integer, unique=False, nullable=False)

    # constructor of a Score object, initializes the instance variables within object (self)
    def __init__(self, username, score1, score2, score3, score4, score5, score6):
        self._username = username
        self._score1 = score1
        self._score2 = score2
        self._score3 = score3
        self._score4 = score4
        self._score5 = score5
        self._score6 = score6

    @property
    def username(self):
        return self._username 
    
    @username.setter
    def username(self, username):
        print("Call username")
        self._username = username
    
 #first score    
    @property
    def score1(self):
        return self._score1

    @score1.setter #for changing each score --> score will be shifted each time new score is added
    def score1(self, score1):
        self._score1 = score1
        
        
#second score

    @property
    def score2(self):
        return self._score2

    @score2.setter
    def score2(self, score2):
        self._score2 = score2

#third score

    @property
    def score3(self):
        return self._score3

    @score3.setter
    def score3(self, score3):
        self._score3 = score3

#fourth score

    @property
    def score4(self):
        return self._score4

    @score4.setter
    def score4(self, score4):
        self._score4 = score4

#fifth score

    @property
    def score5(self):
        return self._score5

    @score5.setter
    def score5(self, score5):
        self._score5 = score5
        
#sixth score

    @property
    def score6(self):
        return self._score6

    @score6.setter
    def score6(self, score6):
        self._score6 = score6
        
    def __str__(self):
        return json.dumps(self.read())

#CRUD --> create 
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            print("Score create method called")
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
#CRUD --> read 
    def read(self):
        return {
            "username": self._username, 
            "score1": self._score1, 
            "score2": self._score2, 
            "score3": self._score3, 
            "score4": self._score4, 
            "score5": self._score5, 
            "score6": self._score6
            }

#CRUD --> update
    def update(self, _username, score):
        self._score1 = score
        self._score2 = self._score1
        self._score3 = self._score2
        self._score4 = self._score3 
        self._score5 = self._score4
        self._score6 = self._score5

def initScores():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        row1 = Scores(username='sreeja', score1=0, score2=0, score3=0, score4=0, score5=0, score6=0)
        row2 = Scores(username='ekam', score1=0, score2=0, score3=0, score4=0, score5=0, score6=0)
        row3 = Scores(username='tirth', score1=0, score2=0, score3=0, score4=0, score5=0, score6=0)
        rows = [row1, row2, row3]

        """Builds sample user/note(s) data"""
        for row in rows:
            try:
                row.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Integrity error")
                