from datetime import timedelta
from flask import request, Response, jsonify
from flask_jwt_extended import create_access_token

from view.base_resource import AccountBaseResource
from model.account import AccountModel


class AuthView(AccountBaseResource):

    def post(self) -> Response:
        payload = request.json
        account: AccountModel = AccountModel.objects(id=payload['id']).first()

        if not account or self.check_password(account.password, payload['password']):
            return Response('wrong account', 204)

        return jsonify({
            'accessToken': create_access_token(account.id, expires_delta=timedelta(hours=1))
        })
