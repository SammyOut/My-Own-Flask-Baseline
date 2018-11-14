from flask import Flask
from flask_jwt_extended import JWTManager
from mongoengine import connect


def create_app(Config):
    app: Flask = Flask(__name__)

    JWTManager(app)

    connect('sample')
    return app
