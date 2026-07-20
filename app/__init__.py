from flask import Flask
from .config import get_config

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    return app
