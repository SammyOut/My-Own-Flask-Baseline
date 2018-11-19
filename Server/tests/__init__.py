from functools import wraps
from json import dumps

from mongoengine.connection import get_connection
from unittest import TestCase

from app import create_app
from config import DevConfig


class TCBase(TestCase):

    def setUp(self):
        self.client = create_app(DevConfig).test_client()

    def tearDown(self):
        connection = get_connection()
        connection.drop_database(DevConfig.DB_NAME)

    def create_account(self, id_='12345', password='12345678', email='python@istruly.sexy'):
        self.client.post(
            '/signup',
            data=dumps(
                dict(id=id_, password=password, email=email)
            ),
            content_type='application/json'
        )


def check_status_code(status_code):
    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            rv = fn(self, *args, **kwargs)
            self.assertEqual(rv.status_code, status_code)
        return wrapper
    return decorator
