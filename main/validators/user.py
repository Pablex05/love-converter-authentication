from main.extensions import db
from main.models import UserModel

from marshmallow import validate


def get_email_existance(email):
    try:
        email_exists = db.session.query(UserModel).filter(UserModel.email == email).scalar() is not None
        if email_exists:
            return 'The entered email address has already been registered', 409
    except validate.ValidationError as e:
        return e, 409
