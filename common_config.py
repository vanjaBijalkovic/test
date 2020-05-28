import os

from name import app_name

SECRET_KEY = 'iQfPvB6sZaNHqVFI5CJa9rM1xOEVHKIM0LwifT04yLsPlZhSSvaDuZXOgJFSpJVq'


class Config:
    NAME = app_name
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    DEBUG = False
    SECURITY_PASSWORD_SALT = 'freenit'
    SECRET_KEY = SECRET_KEY
    SECURITY_TRACKABLE = False
    JWT_SECRET_KEY = SECRET_KEY
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_COOKIE_PATH = '/api/v0'
    JWT_REFRESH_COOKIE_PATH = '/api/v0/auth/refresh'
    JWT_SESSION_COOKIE = False
    JWT_COOKIE_SECURE = True
    OPENAPI_URL_PREFIX = '/doc'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_SWAGGER_UI_PATH = '/swaggerui'
    OPENAPI_SWAGGER_UI_URL = '/static/swaggerui/'
    OPENAPI_VERSION = '3.0.3'
    MEDIA_URL = '/media'
    MEDIA_PATH = 'media'
    ACCOUNT_REQUEST_EXPIRY = 24  # in hours
    PASSWORD_RESET_EXPIRY = 2  # in hours
    DATABASE = {
        'name': 'database.db',
        'engine': 'SqliteDatabase',
    }
    MONGODB_SETTINGS = {
        'host': 'mongodb',
        'db': 'freenit',
    }
    MAIL = {
        #  'host': 'mail.example.com',
        #  'port': 587,
        #  'ssl': True,
        #  'username': 'someone@example.com',
        #  'password': 'Sekrit',
    }
    FROM_EMAIL = 'office@example.com'
    SUBJECTS = {
        'prefix': '[Freenit] ',
        'confirm': 'Account confirmation',
        'register': 'Account registration',
    }

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    SECURITY_SEND_REGISTER_EMAIL = False


class TestConfig(Config):
    TESTING = True
    JWT_COOKIE_SECURE = False
    DATABASE = {
        'name': 'test.db',
        'engine': 'SqliteDatabase',
    }


class ProdConfig(Config):
    pass
