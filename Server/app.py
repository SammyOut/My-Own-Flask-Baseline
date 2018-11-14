from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from mongoengine import connect


def create_app(config):
    app: Flask = Flask(__name__)
    app.config.from_object(config)

    JWTManager(app)
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    connect('sample')
    return app
