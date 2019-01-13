from flask import Flask
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from instance.config import app_config
from .api.v1.views.meetup_view import meetup
from .api.v1.views.questions_view import v1 as questions
from .api.v1.views.user_view import user

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(meetup)
    app.register_blueprint(questions)
    app.register_blueprint(user)
    app.config.from_object(app_config[config])

    # app.config.from_object(confi)
    app.config['JWT_SECRET_KEY'] = "@2ekj@#02ks-"
    jwt= JWTManager(app)
    return app