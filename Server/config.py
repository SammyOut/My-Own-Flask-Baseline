from os import getenv


class Config:

    SERVICE_NAME = 'Nerdy Flask Baseline'
    SERVER_NAME = '0.0.0.0:5000'

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

    DB_NAME = 'sample'
    DB_HOST = '127.0.0.1'
    DB_PORT = 27017
    MONGOENGINE_CONFIG = {
        'db': DB_NAME,
        'host': DB_HOST,
        'port': DB_PORT
    }


class DevConfig(Config):
    SERVER_NAME = '127.0.0.1:5000'
    ENV = 'development'

    DB_NAME = 'sample_test'
    DB_HOST = '127.0.0.1'
    DB_PORT = 27017
    MONGOENGINE_CONFIG = {
        'db': DB_NAME,
        'host': DB_HOST,
        'port': DB_PORT
    }
