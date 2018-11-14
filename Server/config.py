from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY', 'Nerd-Bear')
    JSON_AS_ASCII = False


class DevConfig(Config):
    RUN_SETTING = {
        'host': '127.0.0.1',
        'port': 5000,
        'debug': True
    }


class ProConfig(Config):
    RUN_SETTING = {
        'host': '127.0.0.1',
        'port': 5000,
        'debug': False
    }
