from datetime import date
import os, base64
import json, hashlib, binascii
from __init__ import db
from sqlalchemy.exc import IntegrityError

class Profile(db.Model):
    __tablename__ = 'Profile'
    _username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    _email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = self.new_password(password)