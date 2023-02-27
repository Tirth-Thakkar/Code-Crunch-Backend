from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from flask_restful import Api, Resource, reqparse
from datetime import datetime

from model.users import User
from model.highscores import Highscore
highscore_api = Blueprint('highscore_api', __name__,
                   url_prefix='/api/highscores')

api = Api(highscore_api)

class HighscoresAPI:
    class _Hscore(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            username = body.get('username')
            hscore = body.get('hscore')
            user = User.query.filter((User._username == username)).first
            if username == 'null':
                return {'message': f'error no login'}, 210
            if user is False:
                return {'message': f'error no user'}, 210
            if int(hscore) is False or int(hscore) <= 0:
                return {'message': f'error no hscore'}, 210

            ''' #1: Key code block, setup USER OBJECT '''
            highscore = Highscore(username=username, hscore=hscore)
            user = highscore.create()
            if user:
                return jsonify(user.read())
            return {'message': f'Processed {username}, either a format error or hscore {hscore} is negative or zero'}, 210
    
    class _Retrieve(Resource):
        def get(self):
            highscores = Highscore.query.order_by(Highscore._hscore.desc()).all()
            json_ready = [highscore.read() for highscore in highscores] 
            return jsonify(json_ready)  
    
    class _GetUserHighestScores(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')

            userhighs = Highscore.query.order_by(Highscore._hscore.desc()).all()
            user_hscores = []
            highscore_dict = {}

            for highscore in userhighs:
                if highscore.username == username:
                    highscore_dict['username'] = highscore.username
                    highscore_dict['score'] = highscore.hscore
                    user_hscores.append(highscore_dict)
                    break

                if highscore.username not in highscore_dict:
                    highscore_dict[highscore.username] = highscore.hscore
                    user_hscores.append({'username': highscore.username, 'hscore': highscore.hscore})

            return jsonify(user_hscores)


    api.add_resource(_Hscore, '/hscore')
    api.add_resource(_Retrieve, '/retrieve')
    api.add_resource(_GetUserHighestScores, '/getuserhighestscores')