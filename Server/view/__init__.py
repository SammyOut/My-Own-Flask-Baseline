from flask import Flask
from flask_restful import Api


def register(app: Flask):
    api = Api(app)

    from view.account.signup import SignupView
    from view.account.auth import AuthView
    api.add_resource(SignupView, '/signup')
    api.add_resource(AuthView, '/auth')
