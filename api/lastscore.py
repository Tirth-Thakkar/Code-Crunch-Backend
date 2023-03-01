from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from flask_restful import Api, Resource, reqparse
from datetime import datetime
import json 
import datetime

from __init__ import db

from model.users import User
from model.scores import Scores

score_api = Blueprint('score_api', __name__,
                   url_prefix='/api/lastscore')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(score_api)

class ScoresAPI:       
    class _Score(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            name = body.get('username')
            score = body.get('score')
            ##user = Scores.query.filter((User.username == name)).first
            user = Scores.query.filter_by(_username=str(name)).first()
            ## return {'message': f'user: {user}'}, 210
            if user is None:
                new_user = Scores(username=str(name), score=int(score))
                db.session.add(new_user)
                db.session.commit()
                return {'message': f'Add new user'}, 210
            if int(score) is False or int(score) <= 0:
                return {'message': f'error no score'}, 210            
            #Scores.query.filter_by(username='ekam').update({Scores.score1: 25})
            Scores.query.filter_by(_username=str(name)).update({Scores._score6: Scores._score5})
            Scores.query.filter_by(_username=str(name)).update({Scores._score5: Scores._score4})
            Scores.query.filter_by(_username=str(name)).update({Scores._score4: Scores._score3})
            Scores.query.filter_by(_username=str(name)).update({Scores._score3: Scores._score2})
            Scores.query.filter_by(_username=str(name)).update({Scores._score2: Scores._score1})
            Scores.query.filter_by(_username=str(name)).update({Scores._score1: int(score)})
            db.session.commit()
            ## score.update_lcl(username=username, _score=score);
            #if user:
            #    return jsonify(score.read())
            # failure returns error
            #return {'message': f'Processed {username}, either a format error or score {score} is negative or zero'}, 210

    class _Retrieve(Resource):
        def get(self):
            body = request.get_json()
            name = body.get('username')
            user = Scores.query.filter((User.username == name)).first()
            if name == 'null':
                return {'message': f'error no login'}, 210
            # Query the table, filter by age, order by name, and print each record
            rows = db.session.query(Scores).all()
                # Convert the list of model objects to a list of dictionaries
            data = []
            for row in rows:
                row_dict = row.__dict__
                del row_dict['_sa_instance_state']
                data.append(row_dict)
            return jsonify(data)
            
            ##records = Scores.query.filter_by(_username=str(name)).order_by(Scores.name).all()
            #msg = ""
            # for rec in records:
            #     msg = msg + " id: " + str(rec.id) + ", user: " + str(rec._username)
            # return {'message': f'{msg}'}, 21
    #         leaders = Leader.query.order_by(Leader._score.desc()).limit(10).all()   # read/extract all users from database
    #         json_ready = [leader.read() for leader in leaders]  # prepare output in json
    #         return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
            
    class _GetUserScoresFiltered(Resource):
        def get(self):
            body = request.get_json()
            name = body.get('username')
            user = Scores.query.filter((User.username == name)).first
            if name == 'null':
                return {'message': f'error no login'}, 210
            # Query the table, filter by age, order by name, and print each record
            #rec = db.session.query(Scores._username, Scores._score1, Scores._score2, Scores._score3, Scores._score4, Scores._score5, Scores._score6).filter_by(_username=str(name)).first()
            #msg = rec
            row = db.session.query(Scores).filter_by(_username=str(name)).first()
            row_dict = row.__dict__
            del row_dict['_sa_instance_state']  # Remove the internal state
            return jsonify(row_dict)
            # records = Scores.query.filter_by(username=str(name)).order_by(Scores._username).all()
            # msg = ""
            # for rec in records:
            #    msg = msg + " id: " + str(rec.id) + ", user: " + str(rec._username)
            
            #body = request.get_json()
            # username = body.get('username')
            # userleads = Leader.query.order_by(Leader._score.desc()).all()
            # # Filter leaderboard entries to only include scores for desired user
            # user_scores = [leader.read() for leader in userleads if leader.username == username]
            # if not user_scores:
            #     return {'message': f'No scores found for user {username}'}, 210
            #return jsonify(rec) 
            
            # return {'message': f'{msg}'}, 21
            # leaders = Leader.query.order_by(Leader._score.desc()).all()   # read/extract all users from database
            # json_ready = [leader.read() for leader in leaders]  # prepare output in json
            # return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    #         leaders = Leader.query.order_b
            # body = request.get_json()
            # username = body.get('username')

            # # Retrieve user by username
            # # Retrieve top 10 leaderboard entries, ordered by score
            # userleads = Leader.query.order_by(Leader._score.desc()).limit(10).all()
            # # Filter leaderboard entries to only include scores for desired user
            # user_scores = [{'username': leader.username, 'score': leader.score} for leader in userleads if leader.username == username]

            # return jsonify(user_scores)

            
    # building RESTapi endpoint
    api.add_resource(_Score, '/score')
    api.add_resource(_Retrieve, '/retrieve')
    api.add_resource(_GetUserScoresFiltered, '/getuserscoresfiltered')
    