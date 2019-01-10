from flask import Flask

from instance.config import app_config
from .v1.views.meetup_view import meetup
from .v1.views.questions_view import v1 as questions
from .v1.views.user_view import user

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(meetup)
    app.register_blueprint(questions)
    app.register_blueprint(user)
    app.config.from_object(app_config[config])
    return app