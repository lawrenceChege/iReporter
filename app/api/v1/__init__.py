from flask import Blueprint
from flask_restplus import Api
from app.api.v1.views.redflags import RedFlags, RedFlag
from app.api.v1.views.users import Users, User

version_one = Blueprint("v1", __name__, url_prefix="/api/v1")
API = Api(version_one)


API.add_resource(RedFlags, '/redflags/')
API.add_resource(RedFlag, '/redflags/<int:id>/')
API.add_resource(Users, '/auth/signup/')
API.add_resource(User, '/auth/login/')
