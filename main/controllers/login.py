from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from main.extensions import db
from main.mappers import UserMapper
from main.models import UserModel

user_mapper = UserMapper()


class Login(Resource):

    def post(self):
        entered_email = str(request.get_json().get('email'))
        entered_password = str(request.get_json().get('password'))
        user = db.session.query(UserModel).filter(UserModel.email == entered_email).first_or_404()

        # True value if both passwords match
        if user.validate_password(entered_password):
            access_token = create_access_token(identity=user)
            data = {
                "user": user_mapper.dump(user),
                "token": access_token
            }
            return data, 200
        else:
            return 'You have entered wrong credentials.', 401
