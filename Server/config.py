from os import getenv


class Config:
    SERVICE_NAME = 'Nerdy Flask Baseline'

    SECRET_KEY = getenv('SECRET_KEY', 'Nerd-Bear')
    JSON_AS_ASCII = False

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'basePath': '/',
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Account',
                'description': '계정 관련 API'
            }
        ]
    }


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
