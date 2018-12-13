from flask import Blueprint
from flask_restplus import Api
from app.api.v2.views.incidents import Incidents, Incident, Comment, Location, Status
from app.api.v2.views.users import Users, User
from flask_jwt_extended.exceptions import *

version_two = Blueprint("v2", __name__, url_prefix="/api/v2")
API = Api(version_two)


API.add_resource(Incidents, '/incidents/')
API.add_resource(Incident, '/incidents/<int:incident_id>/')
API.add_resource(Comment, '/incidents/<int:incident_id>/description')
API.add_resource(Location, '/incidents/<int:incident_id>/location')
API.add_resource(Status, '/incidents/<int:incident_id>/status')
API.add_resource(Users, '/auth/signup/')
API.add_resource(User, '/auth/login/')


@API.errorhandler
def default_error_handler(error):
    '''Default error handler'''
    return {'message': str(error)}, getattr(error, 'code', 500)


@API.errorhandler(NoAuthorizationError)
def handle_Missing_Token_exception(error):
    '''Return a custom message and 400 status code'''
    return {'message': str(error)}, 401

