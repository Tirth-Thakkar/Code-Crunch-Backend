from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from flask_restful import Api, Resource, reqparse
from datetime import datetime

from model.users import User
from model.leaders import Leader
leader_api = Blueprint('leader_api', __name__,
                   url_prefix='/api/leadersfiltered')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(leader_api)

class LeadersAPI:       
    class _Score(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            username = body.get('username')
            score = body.get('score')
            user = User.query.filter((User.username == username)).first
            if username == 'null':
                return {'message': f'error no login'}, 210
            if user is False:
                return {'message': f'error no user'}, 210
            if int(score) is False or int(score) <= 0:
                return {'message': f'error no score'}, 210
        
            ''' #1: Key code block, setup USER OBJECT '''
            leader = Leader(username=username, score=score)
            # create user in database
            user = leader.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {username}, either a format error or score {score} is negative or zero'}, 210

    class _Retrieve(Resource):
        def get(self):
            leaders = Leader.query.order_by(Leader._score.desc()).limit(10).all()   # read/extract all users from database
            json_ready = [leader.read() for leader in leaders]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
            
    class _GetUserScoresFiltered(Resource):
        def post(self):
            body = request.get_json()
            username = body.get('username')
            userleads = Leader.query.order_by(Leader._score.desc()).all()
            # Filter leaderboard entries to only include scores for desired user
            user_scores = [{'username': leader.username, 'score': leader.score} for leader in userleads if leader.username == username]
            if not user_scores:
                return {'message': f'No scores found for user {username}'}, 404
            return jsonify(user_scores)

            
    # building RESTapi endpoint
    api.add_resource(_Score, '/score')
    api.add_resource(_Retrieve, '/retrieve')
    api.add_resource(_GetUserScoresFiltered, '/getuserscoresfiltered')
    