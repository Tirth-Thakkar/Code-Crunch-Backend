# Remove: from datetime import datetime
from flask import make_response, abort

from config import db
from models import User, user_schema, users_schema


# Remove: get_timestamp():
# Remove: USER --> not a defined variable so i put this in comments for now until i find out where it came from (EK)

# ...

def create(user):
    username = user.get("username")
    existing_user = User.query.filter(User.username == username).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(406, f"Person with username {username} already exists")


def update(username, user):
    existing_user = User.query.filter(User.username == username).one_or_none()

    if existing_user:
        update_user = user_schema.load(user, session=db.session)
        existing_user.email = update_user.email
        db.session.merge(existing_user)
        db.session.commit()
        return user_schema.dump(existing_user), 201
    else:
        abort(404, f"Person with username {username} not found")

def delete(username):
    existing_user = User.query.filter(User.username == username).one_or_none()

    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f"{username} successfully deleted", 200)
    else:
        abort(404, f"Person with username {username} not found")