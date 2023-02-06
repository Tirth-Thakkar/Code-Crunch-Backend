""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json, hashlib, binascii

from __init__ import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash



class Player(db.model):
    __tablename__ = 'players'
    _username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    _email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = self.new_password(password)
    
    @property
    def user_info(self):
        return {
            'username': self._username,
            'email': self._email,
            'password': self._password[0:3] + '...'
        }
    
    # To set new username
    def new_username(self, newname):
        self._username = newname
    
    # To set new email
    def new_email(self, newemail):
        self._email = newemail
    
    # To set new password
    def new_password(newpass):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        hashed_password = hashlib.pbkdf2_hmac('sha512', newpass.encode('utf-8'), salt, 100000)
        hashed_password = binascii.hexlify(hashed_password)
        encrypted_pass = (salt + hashed_password).decode('ascii')
        return encrypted_pass

    # To Check if the password is correct
    def password_validation(self, check_pass):
        salt = self._password[:64]
        check_pass_hash = hashlib.pbkdf2_hmac('sha512', check_pass.encode('utf-8'), salt.encode('ascii'), 100000)
        check_pass_hash = binascii.hexlify(check_pass_hash).decode('ascii')
        return check_pass_hash == self._password[64:]

    def new_user(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None
