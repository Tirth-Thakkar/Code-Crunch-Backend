from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource 
import os
from model.userdata import Player
from datetime import datetime

login_system = Blueprint('user_api', __name__, url_prefix='/api/user-data')

api = Api(login_system)

class LoginReg:
    class SignUp(Resource):
        def post(self):
            body = request.get_json()
            name = body.get('username')
            uid = body.get('uid')
            email = body.get('email')
            password = body.get('password')
            
            uo = Player(name=name, uid=uid)
            
            if password is not None:
                uo.set_password(password)
            
            user = uo.create()
            if user:
                return jsonify(user.read())
            return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 210

