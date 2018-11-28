from flask import Flask, Blueprint

from api.v1 import version_one as v1

def create_app():
    APP= Flask(__name__)
    APP.register_blueprint(v1)
    return APP