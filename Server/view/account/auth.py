from flask import request, Response

from view import AccountBaseResource
from model.account import AccountModel


class AuthView(AccountBaseResource):

    def post(self) -> Response:
        payload = request.json
        account: AccountModel = AccountModel.objects(id=payload['id']).first()

        if not account or self.check_password(account.password, payload['password']):
            return Response('wrong account', 204)

        return Response('success', 200)
