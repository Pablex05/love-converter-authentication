from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token

from main.mappers import UserMapper
from main.models import UserModel
from main.extensions import db

user_mapper = UserMapper()


class Login(Resource):

    def post(self):
        entered_email = str(request.get_json().get('email'))
        entered_password = str(request.get_json().get('password'))
        user = db.session.query(UserModel).filter(UserModel.email == entered_email).first_or_404()

        passwords_match = user.validate_password(entered_password)
        # True value if both passwords match

        if passwords_match:

            access_token = create_access_token(identity=user)

            data = {
                "user": user_mapper.dump(user),
                "token": access_token
            }

            return data, 200
        else:
            return 'You have entered wrong credentials.', 401
