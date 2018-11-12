class Config:
    pass


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
