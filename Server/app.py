from flask import Flask
from mongoengine import connect


def create_app(Config):
    app: Flask = Flask(__name__)

    connect('sample')
    return app
