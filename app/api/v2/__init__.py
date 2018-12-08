from flask import Blueprint
from flask_restplus import Api
from app.api.v2.views.incidents import Incidents, Incident, Comment, Location
from app.api.v2.views.users import Users, User

version_two = Blueprint("v2", __name__, url_prefix="/api/v2")
API = Api(version_two)


API.add_resource(Incidents, '/incidents/')
API.add_resource(Incident, '/incidents/<int:incident_id>/')
API.add_resource(Comment, '/incidents/<int:incident_id>/description')
API.add_resource(Location, '/incidents/<int:id>/location')
API.add_resource(Users, '/auth/signup/')
API.add_resource(User, '/auth/login/')
