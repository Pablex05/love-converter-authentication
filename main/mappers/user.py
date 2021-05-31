from marshmallow import validate
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from main.models import UserModel


class User(SQLAlchemySchema):
    class Meta:
        model = UserModel
        include_relationships = True
        load_instance = True
        ordered = True

    id = auto_field(dump_only=True)  # Read from db only
    username = auto_field(required=True)
    email = auto_field(required=True, validate=validate.Email())
    deleted = auto_field(required=True)
    activated = auto_field(required=True)
    last_updated = auto_field(required=True)
    last_access = auto_field(required=True)
