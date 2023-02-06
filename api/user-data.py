from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource 
import os

login_system = Blueprint('user_api', __name__, url_prefix='/api/user-data')

api = Api(login_system)

class LoginReg:
    class SignUp(Resource):
        def post(self):
            body = request.get_json()
            name = body.get('username')
            email = body.get('email')
            password = body.get('password')
            
            uo = User(name=name, uid=uid)
            
            if password is not None:
                uo.set_password(password)
            if dob is not None:
                try:
                    uo.dob = datetime.strptime(dob, '%m-%d-%Y').date()
                except:
                    return {'message': f'Date of birth format error {dob}, must be mm-dd-yyyy'}, 210
            
            user = uo.create()
            if user:
                return jsonify(user.read())
            return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 210

