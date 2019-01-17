from flask import Flask
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from instance.config import app_config
from .api.v1.views import meetup_view,questions_view,user_view
from .api.v2.views.meetup_view import meetup_v2
from .api.v2.views.user_view import user_v2,auth_v2
from .api.v2.views.questions_view import v2 as question_v2

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)

    # register blueprints
    app.register_blueprint(meetup_view.meetup)
    app.register_blueprint(questions_view.v1)
    app.register_blueprint(user_view.user)
    app.register_blueprint(user_view.auth)
    app.register_blueprint(question_v2)
    app.register_blueprint(meetup_v2)
    app.register_blueprint(user_v2)
    app.register_blueprint(auth_v2)
    app.config.from_object(app_config[config])

    # app.config.from_object(confi)
    app.config['JWT_SECRET_KEY'] = "@2ekj@#02ks-"
    # jwt= JWTManager(app)
    
    return app