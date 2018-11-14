from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from mongoengine import connect

from view import register


def create_app(config) -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(config)

    JWTManager(app)
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    register(app)
    connect('sample')
    return app
