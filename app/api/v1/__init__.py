from flask import Blueprint
from flask-restplus import Api
from views.redflags import RedFlags, RedFlag, Users

version_one = Blueprint("v1", __name__, url_prefix="/api/v1")
API = Api(version_one)


API.add_resource(RedFlags, '/redflags/')
API.add_resource(RedFlag, '/redflags/<int:id>'/)
API.add_resource(Users, '/auth/signup/)
