import re
from flask import request, Response
from flasgger import swag_from

from view.base_resource import AccountBaseResource
from model.account import AccountModel
from docs.account.signup import SIGNUP_POST


class SignupView(AccountBaseResource):

    @swag_from(SIGNUP_POST)
    def post(self) -> Response:
        payload = request.json

        if AccountModel.objects(id=payload['id']).first():
            return Response('Id already exist.', 205)

        if not 5 <= len(payload['id']) <= 20:
            return Response('Wrong id length', 205)

        if not 8 <= len(payload['password']) <= 32:
            return Response('Wrong password length')

        email_regex = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
        if not re.match(email_regex, payload['email']):
            return Response('Wrong email format', 205)

        encrypted_password = self.encrypt_password(payload['password'])
        AccountModel(id=payload['id'], password=encrypted_password, email=payload['email']).save()
        return Response('', 201)
