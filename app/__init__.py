from flask import Flask
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from instance.config import app_config
from .api.v1 import views as v1_views
from .api.v2 import views as v2_views
def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)

    # register blueprints
    app.register_blueprint(v1_views.meetup_view)
    app.register_blueprint(v2_views.meetup_view)
    app.register_blueprint(v1_views.questions_view.v1)
    app.register_blueprint(v2_views.questions_view.v2)
    app.register_blueprint(v1_views.user_view)
    app.register_blueprint(v2_views.user_view)
    app.config.from_object(app_config[config])

    # app.config.from_object(confi)
    app.config['JWT_SECRET_KEY'] = "@2ekj@#02ks-"
    # jwt= JWTManager(app)
    
    return app