"""
    This module cnfigures how the app will run
""" 
import datetime
from flask import Flask, Blueprint
from flask_restplus import Api
from flask_jwt_extended import JWTManager
from instance.config import config
from app.api.v1 import version_one as v1
from app.api.v2 import version_two as v2
from app.api.errors import errors as e


timeout = datetime.timedelta(300)

def create_app(config_name):
    """
        This function creates a flask app and
        registers api version blueprints 
    """
    
    APP = Flask(__name__, instance_relative_config=True)
    APP.config.from_object(config[config_name])
    APP.config['JWT_SECRET_KEY'] = 'fcv gzxcv62ws'
    APP.config['JWT_ACCESS_TOKEN_EXPIRES'] = timeout
    jwt = JWTManager(APP)
    APP.register_blueprint(v1)
    APP.register_blueprint(v2)
    APP.register_blueprint(e)
    APP.url_map.strict_slashes = False

    @jwt.expired_token_loader
    def my_expired_token_callback():
        return {
            'status': 401,
            'sub_status': 42,
            'error': 'The token has expired'
        }, 401

    @jwt.unauthorized_loader
    def my_unauthorized_callback():
        return {
            'status': 401,
            'sub_status': 43,
            'error': 'Missing token'
        }, 401

   
    return APP


