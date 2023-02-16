from localStoragePy import localStoragePy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy()

localStorage = localStoragePy('app-namespace', 'sqlite')


import json 

print("hello")

class Graphs(db.Model):
    __tablename__ = 'graph_scores' 
   
    username = db.Column(db.String(255), unique=True, primary_key=True)
    score1 = db.Column(db.Integer, unique=False, nullable=False)
    score2 = db.Column(db.Integer, unique=False, nullable=False)
    score3 = db.Column(db.Integer, unique=False, nullable=False)
    score4 = db.Column(db.Integer, unique=False, nullable=False)
    score5 = db.Column(db.Integer, unique=False, nullable=False)
    score6 = db.Column(db.Integer, unique=False, nullable=False)

    def init(self, username, score1, score2, score3, score4, score5, score6, score7, score8):
        self.username = username
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.score4 = score4
        self.score5 = score5
        self.score6 = score6

    @property
    def username(self):
        return self.username 
    
 #first score    
    @property
    def score1(self):
        return self.score1

    @score1.setter #for changing each score --> score will be shifted each time new score is added
    def score1(self, score1):
        self.score1 = score1
        
#second score

    @property
    def score2(self):
        return self.score2

    @score2.setter
    def score2(self, score2):
        self.score2 = score2

#third score

    @property
    def score3(self):
        return self.score3

    @score3.setter
    def score3(self, score3):
        self.score3 = score3

#fourth score

    @property
    def score4(self):
        return self.score4

    @score4.setter
    def score4(self, score4):
        self.score4 = score4

#fifth score

    @property
    def score5(self):
        return self.score5

    @score5.setter
    def score5(self, score5):
        self.score5 = score5
        
#sixth score

    @property
    def score6(self):
        return self.score6

    @score6.setter
    def score6(self, score6):
        self.score6 = score6


    def read(self):
        return {"username": self.username, "score1": self.score1, "score2": self.score2, "score3": self.score3, "score4": self.score4, "score5": self.score5, "score6": self.score6}
    
    def __str__(self):
        return json.dumps(self.read())

    def create(self):
            db.session.add(self) 
            db.session.commit()
            return self
    
    def update(self, username, score1, score2, score3, score4, score5, score6):
        new_score = localStorage.getItem("lowScore")
        score1 = score2 
        score2 = score3 
        score3 = score4 
        score4 = score5 
        score5 = score6 
        score6 = new_score
        
