from flask import request
from flask_restful import Resource

from main.extensions import db
from main.mappers import UserMapper
from main.models import UserModel
from main.validators import email_validator
from main.services import UserService

user_mapper = UserMapper()


class Register(Resource):

    @staticmethod
    def post(self):
        json = request.get_json()
        email_validator(json["email"])

        # TODO: Refactor to repositories
        if json != "":
            user_instance = UserModel(
                email=json.get("email"),
                plain_password=json.get("password"),
                username=json.get("username"),
                deleted=False,
                activated=False,
                last_updated=json.get("last_updated"),
                last_access=json.get("last_access")
            )
            # TODO: Define last updated and last access methods

            db.session.add(user_instance)
            try:
                db.session.commit()
                return 'Done. Please activate your account in order to sign in', 201
            except Exception as error:
                db.session.rollback()
                print("\nUser operation error: ", error)
                return 'Error in operation', 409
