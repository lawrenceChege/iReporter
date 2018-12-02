"""
    This module cnfigures how the app will run
"""
from flask import Flask, Blueprint
from flask_restplus import Api
from instance.config import config

from app.api.v1 import version_one as v1

def create_app(config_name):
    """
        This function creates a flask app and
        registers api version blueprints 
    """
    APP= Flask(__name__, instance_relative_config=True)
    # APP.config.from_object(config[config_name])
    APP.config.from_pyfile('config.py')
    APP.register_blueprint(v1)
    return APP




