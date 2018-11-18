from json import dumps

from pymongo import MongoClient
from unittest import TestCase

from app import create_app
from config import TestConfig


class TCBase(TestCase):

    def setUp(self):
        self.client = create_app(TestConfig).test_client()

        self.mongo_client = MongoClient(**TestConfig.PYMONGO_CONFIG)
        self.db = self.mongo_client[TestConfig.DB_NAME]

    def tearDown(self):
        self.mongo_client.drop_database(TestConfig.DB_NAME)

    def create_account(self, id_='12345', password='12345678', email='python@istruly.sexy'):
        self.client.post(
            '/signup',
            data=dumps(
                dict(id=id_, password=password, email=email)
            ),
            content_type='application/json'
        )
