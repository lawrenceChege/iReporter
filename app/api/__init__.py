from flask import Flask
from flask_restplus import Api
from api.v1.views import version_one as v1

APP = Flask(__name__)
API = Api(APP)

API.register_blueprint(v1)
