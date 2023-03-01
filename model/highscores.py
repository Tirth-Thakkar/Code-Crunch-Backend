# from random import randrange
# from datetime import date
# import os, base64
# import json


# from __init__ import app, db
# from sqlalchemy.exc import IntegrityError


# class Highscore(db.Model):
#     __tablename__ = 'highscores'
#     id = db.Column(db.Integer, primary_key=True)
#     _username = db.Column(db.String(255))
#     _hscore = db.Column(db.Integer, unique=False, nullable=False)


#     def __init__(self, username, hscore):
#         self._username = username
#         self._hscore = hscore


#     @property
#     def username(self):
#         return self._username
   
#     @username.setter
#     def username(self, username):
#         self._username = username
   
#     @property
#     def hscore(self):
#         return self._hscore


#     @hscore.setter
#     def hscore(self, hscore):
#         self._hscore = hscore


#     def __str__(self):
#         return json.dumps(self.read())


#     def create(self):
#         try:
#             db.session.add(self)
#             db.session.commit()
#             return self
#         except IntegrityError:
#             db.session.remove()
#             return None


#     def read(self):
#         return {'username': self.username, 'hscore': self.hscore}


#     def update(self, username, hscore):
#         if username != "null" and username != None:
#             self.username = username
#         if hscore >= 0:
#             self.hscore = hscore
#         return self


#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#         return None
   
# def initHighscores():
#     with app.app_context():
#         """Create database and tables"""
#         db.init_app(app)
#         db.create_all()
#         """Tester data for table"""
#         highscore1 = Highscore(username='sreeja', hscore=7)
#         highscore2 = Highscore(username='ekam', hscore=7)
#         highscore3 = Highscore(username='tirth', hscore=7)
#         highscore4 = Highscore(username='mani', hscore=7)
#         highscore5 = Highscore(username='user', hscore=7)
#         highscores = [highscore1, highscore2, highscore3, highscore4, highscore5]




#         """Builds sample user/note(s) data"""
#         for highscore in highscores:
#             try:
#                 highscore.create()
#             except IntegrityError:
#                 '''fails with bad or duplicate data'''
#                 db.session.remove()
#                 print(f"Records exist, duplicate email, or error: {highscore.username}")
            