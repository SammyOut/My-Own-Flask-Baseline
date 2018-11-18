from json import dumps

from mongoengine.connection import get_connection
from unittest import TestCase

from app import create_app
from config import TestConfig


class TCBase(TestCase):

    def setUp(self):
        self.client = create_app(TestConfig).test_client()

    def tearDown(self):
        connection = get_connection()
        connection.drop_database(TestConfig.DB_NAME)

    def create_account(self, id_='12345', password='12345678', email='python@istruly.sexy'):
        self.client.post(
            '/signup',
            data=dumps(
                dict(id=id_, password=password, email=email)
            ),
            content_type='application/json'
        )
