from model import *


class AccountModel(Document):
    id = StringField(
        primary_key=True,
        min_length=5,
        max_length=20
    )

    password = StringField(
        required=True,
        min_length=8,
        max_length=32
    )

    email = StringField(
        required=True,
        regex='^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
    )
