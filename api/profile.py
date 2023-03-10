from flask import Blueprint, request, jsonify, abort, Flask
from flask_restful import Api, Resource #used for REST API building
from flask_restful import Api, Resource
from model.users import User
from model.profiles import Profile
profile_api = Blueprint('profile_api', __name__,
                   url_prefix='/api/profilesfiltered')

app = Flask(__name__)
api = Api(profile_api)

class ProfilesAPI:       
    class _Update(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            username = body.get('username')
            email = body.get('email')
            high_score = body.get('high_score')
            starred_games = body.get('starred_games')
            points_per_second = body.get('points_per_second')
            user = User.query.filter((User.username == username)).first
            
            if username == 'null':
                return {'message': f'error no login'}, 210
            if user is False:
                return {'message': f'error no user'}, 210
            if email is False:
                return {'message': f'error no email'}, 210
            if int(high_score) is False or int(high_score) < 0:
                return {'message': f'error no high score'}, 210
            if int(starred_games) is False or int(starred_games) < 0:
                return {'message': f'error no starred games'}
            if int(points_per_second) is False or int(points_per_second) < 0:
                return {'message': f'error no points per second'}
            
            ''' #1: Key code block, setup USER OBJECT '''
            profile = Profile(username=username, email=email, high_score=int(high_score), starred_games=int(starred_games), points_per_second=int(points_per_second))
            #create user in database
            user = profile.create()
            #success returns json of user
            if user:
                return jsonify(user.read())
            else:
                return {'message': "integrity"}, 210
            # f'Either your username {username}, email {email}, high score {high_score}, starred games {starred_games}, or points per second {points_per_second} is problematic or less than zero.'
    class _Read(Resource):
        def get(self):
            profiles = Profile.query.all()    #read/extract all users from database
            json_ready = [profile.read() for profile in profiles]  #prepare output in json
            return jsonify(json_ready)  #jsonify creates Flask response object, more specific to APIs than json.dumps
                    
    api.add_resource(_Update, '/update')
    api.add_resource(_Read, '/read')