from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Database principal initialization
db = SQLAlchemy()

# Authentication handler principal initialization
jwt = JWTManager()
