from flask import Flask
from pymongo import MongoClient
from unittest import TestCase

from app import create_app
from config import ProConfig


class TCBase(TestCase):

    def __init__(self):
        super(TestCase, self).__init__()

        self.client = create_app(ProConfig).test_client()

        self.db_name = 'sample_test'
        self.mongo_client = MongoClient()
        self.db = self.mongo_client[self.db_name]

    def tearDown(self):
        self.mongo_client.drop_database(self.db_name)
