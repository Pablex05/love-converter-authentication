import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_cors import CORS

from main.config import DevelopmentConfig

from main.extensions import db, jwt

# Flask API RESTFUL principal initialization
api = Api()

# Loading environment variables
load_dotenv()


# Function that activates primary keys recognition in the SQLite DB
def activate_primary_keys(connection, _connection_record):
    connection.execute('pragma foreign_keys=ON')


# Function that creates an instance of the Flask application, summing other complements
def create_app():
    # Flask app initialization
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig())


    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    # Database initialization in Flask app
    db.init_app(app)

    # JWT management initialization in Flask app
    jwt.init_app(app)

    # Flask CORS configuration to allow access
    CORS(app, resources={r"/*": {"origins": "*", "expose_headers":  ['X-Total-Count']}})

    # When the database is "connected in Flask app, the primary keys will activate"
    with app.app_context():
        from sqlalchemy import event
        # event.listen(db.engine, 'connect', activate_primary_keys)
        pass
    # TODO: Connect db

    # Final app initialization
    api.init_app(app)

    return app
