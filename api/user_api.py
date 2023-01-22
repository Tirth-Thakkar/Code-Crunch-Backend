from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from model.users import User

user_api = Blueprint('user_api', name)

@user_api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    if not email or not username or not password:
        return jsonify({'message': 'Missing field(s)'}), 400
    if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400
    user = User(email=email, username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@user_api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'message': 'Missing field(s)'}), 400
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'message': 'Login successful'}), 200