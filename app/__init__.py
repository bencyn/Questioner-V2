from flask import Flask

from instance.config import app_config
from .v1.views.meetup_view import meetup

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(meetup)
    app.config.from_object(app_config[config])
    return app