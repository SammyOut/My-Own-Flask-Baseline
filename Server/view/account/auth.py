from datetime import timedelta
from flask import request, Response, jsonify
from flask_jwt_extended import create_access_token
from flasgger import swag_from

from view.base_resource import AccountBaseResource
from model.account import AccountModel
from docs.account.auth import AUTH_POST


class AuthView(AccountBaseResource):

    @swag_from(AUTH_POST)
    def post(self) -> Response:
        payload = request.json
        account: AccountModel = AccountModel.objects(id=payload['id']).first()

        if not account or not self.check_password(account.password, payload['password']):
            return Response('wrong account', 204)

        return jsonify({
            'accessToken': create_access_token(account.id, expires_delta=timedelta(hours=1))
        })
