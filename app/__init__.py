"""
    This module cnfigures how the app will run
""" 
import datetime
from flask import Flask, Blueprint
from flask_restplus import Api
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound
from instance.config import config
from app.api.v1 import version_one as v1
from app.api.v2 import version_two as v2
from migrations import DbModel


timeout = datetime.timedelta(30)

def create_app(config_name):
    """
        This function creates a flask app and
        registers api version blueprints 
    """
    
    APP = Flask(__name__, instance_relative_config=True)
    APP.config.from_object(config[config_name])
    jwt = JWTManager(APP)
    APP.register_blueprint(v1)
    APP.register_blueprint(v2)
    APP.config['JWT_ACCESS_TOKEN_EXPIRES'] = timeout
    APP.config['JWT_SECRET_KEY'] = '123rfgbrf776yt'
    APP.url_map.strict_slashes = False

    @APP.errorhandler(NotFound)
    def handle_Bad_Request(error):  
        '''Return a custom message and 404 status code'''
        return {'ststus':404, 'error': 'There is nothing here'}, 404
      
    return APP
