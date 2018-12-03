from flask import Blueprint
from flask_restplus import Api
from app.api.v1.views.redflags import Incidents, Incident, Comment, Location
from app.api.v1.views.users import Users, User

version_one = Blueprint("v1", __name__, url_prefix="/api/v1")
API = Api(version_one)


API.add_resource(Incidents, '/incidents/')
API.add_resource(Incident, '/incidents/<int:id>/')
API.add_resource(Comment, '/incidents/<int:id>/description')
API.add_resource(Location, '/incidents/<int:id>/location')
API.add_resource(Users, '/auth/signup/')
API.add_resource(User, '/auth/login/')
