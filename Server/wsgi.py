from app import create_app

from config import ProConfig

app = create_app(ProConfig)

if __name__ == '__main__':

    app.run(app.config['RUN_SETTING'])