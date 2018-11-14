from model import *


class AccountModel(Document):
    id = StringField(
        primary_key=True,
        min_length=5,
        max_length=20
    )

    password = StringField(
        required=True
    )

    email = StringField(
        required=True,
        regex='^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
    )
