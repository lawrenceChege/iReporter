from flask import Flask, Blueprint
from flask_restplus import Api

from app.api.v1 import version_one as v1

def create_app():
    APP= Flask(__name__)
    API = Api(APP)
    APP.register_blueprint(v1)
    return APP




