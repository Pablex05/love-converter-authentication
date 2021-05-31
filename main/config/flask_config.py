import os


class Config(object):
    """Base config, uses staging database server."""
    DEBUG = os.getenv('DEBUG')
    TESTING = os.getenv('TESTING')
    DB_SERVER = os.getenv('DB_SERVER_IP')

    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    # Secret key for encryption and time of expiration for each access token
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')


# This classes heredate from Config
class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = '192.168.19.32'


class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True


class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
