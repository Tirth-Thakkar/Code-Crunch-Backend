from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class Leader(db.Model):
    __tablename__ = 'leaderboard' 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    score = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, username, score):
        self.username = username
        self.score = score

    @property
    def username(self):
        return self._username
    
    # a setter function, allows name to be updated after initial object creation
    @username.setter
    def username(self, username):
        self._username = username
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        with app.app_context():
            try:
                # creates a person object from User(db.Model) class, passes initializers
                db.session.add(self)  # add prepares to persist person object to Users table
                db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
                return self
            except IntegrityError:
                db.session.remove()
                return None

    def read(self):
        return {'username': self.username, 'score': self.score}

    def update(self, username, score):
        if username != "null" and username != None:
            self.username = username
        if score >= 0:
            self.score = score
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    def initLeaders(self):
        with app.app_context():
            db.create_all()
            db.session.commit()
            db.session.remove()
            return None
def initLeaders():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        leader1 = Leader(username='sreeja', score=5)
        leader2 = Leader(username='ekam', score=4)
        leader3 = Leader(username='tirth', score=3)
        leader4 = Leader(username='mani', score=2)
        leader5 = Leader(username='user', score=1)
        leaders = [leader1, leader2, leader3, leader4, leader5]


        """Builds sample user/note(s) data"""
        for leader in leaders:
            try:
                leader.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {leader.username}")
                
