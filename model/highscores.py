from random import randrange
from datetime import date
import os, base64
import json


from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Highscore(db.Model):
    __tablename__ = 'highscores'
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(db.String(255))
    _score = db.Column(db.Integer, unique=False, nullable=False)


    def __init__(self, username, score):
        self._username = username
        self._score = score


    @property
    def username(self):
        return self._username
   
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


    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
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
   
def initHighscores():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        highscore1 = Highscore(username='sreeja', score=7)
        highscore2 = Highscore(username='ekam', score=7)
        highscore3 = Highscore(username='tirth', score=7)
        highscore4 = Highscore(username='mani', score=7)
        highscore5 = Highscore(username='user', score=7)
        highscores = [highscore1, highscore2, highscore3, highscore4, highscore5]




        """Builds sample user/note(s) data"""
        for highscore in highscores:
            try:
                highscore.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {highscore.username}")
            