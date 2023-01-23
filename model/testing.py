from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_email(cls,email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def check_password(cls,password,password_hash):
        return check_password_hash(password_hash,password)
    
    @classmethod
    def create_user(cls,username,email,password):
        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        
    @classmethod
    def get_all_users(cls):
        return cls.query.all()
