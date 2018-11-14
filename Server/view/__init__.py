from flask_restful import *
from werkzeug.security import generate_password_hash, check_password_hash


class BaseResource(Resource):
    pass


class AccountBaseResource(BaseResource):

    def encrypt_password(self, password: str) -> str:
        return generate_password_hash(password)

    def check_password(self, encrypted_password: str, password: str) -> bool:
        return check_password_hash(encrypted_password, password)
