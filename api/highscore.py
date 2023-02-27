from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from flask_restful import Api, Resource, reqparse
from datetime import datetime


from model.users import User
from model.highscores import Highscore


highscore_api = Blueprint('highscore_api', __name__,
                   url_prefix='/api/highscores')


api = Api(highscore_api)


class HighscoreList(Resource):
    def get(self):
        highscores = Highscore.query.order_by(Highscore._score.desc()).limit(10).all()
        return jsonify([highscore.read() for highscore in highscores])


    def post(self):
        data = request.get_json()
        username = data.get('username')
        score = data.get('score')
        if not username or not score:
            return {'error': 'username and score are required'}, 400
        highscore = Highscore(username=username, score=score)
        highscore.create()
        return jsonify(highscore.read()), 201


class HighscoreDetail(Resource):
    def get(self, id):
        highscore = Highscore.query.filter_by(id=id).first()
        if not highscore:
            return {'error': 'highscore not found'}, 404
        return jsonify(highscore.read())


    def put(self, id):
        data = request.get_json()
        username = data.get('username')
        score = data.get('score')
        highscore = Highscore.query.filter_by(id=id).first()
        if not highscore:
            return {'error': 'highscore not found'}, 404
        highscore.update(username=username, score=score)
        return jsonify(highscore.read())


    def delete(self, id):
        highscore = Highscore.query.filter_by(id=id).first()
        if not highscore:
            return {'error': 'highscore not found'}, 404
        highscore.delete()
        return '', 204


api.add_resource(HighscoreList, '/highscorelist')
api.add_resource(HighscoreDetail, '/highscoredetail')
