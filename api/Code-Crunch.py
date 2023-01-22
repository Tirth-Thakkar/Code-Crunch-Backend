from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash

from database_file import User, db


app = Flask(__name__)
login_registation_api = Blueprint('login_registation_api', __name__, url_prefix='/api/login_registation')
api = Api(login_registation_api)

class login_registration:
    class Registration(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            password = body.get('password')
            email = body.get('email')

            existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
            if existing_user:
                return {'message': 'User already exists'}, 400

            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            return {'message': 'User created successfully'}, 201

    class Login(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            password = body.get('password')

            user = User.query.filter_by(username=username).first()
            if not user:
                return {'message': 'User does not exist'}, 400

            if check_password_hash(user.password, password):
                return {'message': 'Logged in successfully'}, 200
            else:
                return {'message': 'Incorrect password'}, 400
    class Users(Resource):
        def get(self):
            users = User.query.all()
            user_list = [{'username': user.username, 'email': user.email} for user in users]
            return {'users': user_list}

    
    api.add_resource(Registration, '/regsiter')
    api.add_resource(Login, '/Login')
    api.add_resource(Users, '/users')