from datetime import datetime 
from config import db

class User(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True) #unique=True means that every object created for this class will be identified by the username -- username can't be the same as password or email it must be UNIQUE
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))
    timestamp = db.Column( # I have no idea why we need a time stamp here, but the website added it and this doesn't work without it so.. (EK)
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

user_schema = UserSchema()
users_schema = UserSchema(many=True)