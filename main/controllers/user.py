from flask import request
from flask_restful import Resource

from main.extensions import db
from main.mappers import UserMapper
from main.models import UserModel
from main.validators import email_validator

user_mapper = UserMapper()


class User(Resource):

    def get(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        return user.to_json()

    def put(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        data = request.get_json().items()

        for key, value in data:
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201

    def delete(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return 'User deleted successfully', 204
