from flask_restful import Resource
from flask import request

from main.mappers import UserMapper
from main.validators import email_validator
from main.models import UserModel
from main.extensions import db

user_mapper = UserMapper()

"""
    In order to make CRUD methods, we instance the USerRepository class.
"""


class User(Resource):

    # SIGN UP
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
                return user_mapper.dump(self.__model_instance), 201
            except Exception as error:
                db.session.rollback()
                print("\nUser operation error: ", error)
                return 'Error in operation', 409
