from flask import Flask


def create_app(Config):
    app: Flask = Flask(__name__)

    return app
