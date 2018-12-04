""" These module deals with redflag methods and routes"""
import datetime
from flask_restplus import Resource, reqparse, Api
from flask import request, jsonify,Flask
from flask_jwt_extended import jwt_required
from app.api.v1.models.redflags import IncidentsModel

# from app.api.v1.validators.validators import Validate

app =Flask(__name__)
API = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument("title",
                    type=str,
                    required=True,
                    help="title field is required.")
parser.add_argument("description",
                    type=str,
                    required=True,
                    help="description field is required.")
parser.add_argument("IncidentType",
                    type=str,
                    help="Type field is required.")
parser.add_argument("images",
                    type=str,
                    help="images field is optional.")
parser.add_argument("video",
                    type=str,
                    help="video field is optional.")
parser.add_argument("location",
                    type=str,
                    help="location field is optional.")


class Incidents(Resource):
    """
        This class has methods for posting redflags and getting all redflags posted
    """

    @jwt_required
    @API.doc(params={'title': 'The title of the incident',
                     'type': 'Redflag or Intervention',
                     'description': 'The general description of the incident',
                     'images': 'The link to the image',
                     'video': 'the link to the video',
                     'location': 'the location coordinates'})
    def post(self):
        """
            This method  posts an incident to the databse
        """

        # self.validate = Validate()
        self.model = IncidentsModel()
        self.parse = parser.parse_args()

        new_redflag = self.model.post_incident()
        if new_redflag:
            return jsonify({"status": 201, "data": [{
                "RedFlag_id": new_redflag,
            }],
                "message": "Redflag posted successfully!"})
        return jsonify({"status": 400, "error": "Redflag already exists"})

    @API.doc('List all Incidents')
    def get(self):
        """ 
            This method retrives all the posted incidents from the database
        """
        self.model = IncidentsModel()
        redflags = self.model.get_all_incidents()
        return jsonify({"status": 200,
                        "data": [{
                            "RedFlags": redflags,
                        }],
                        "message": "All redflags found successfully"})


class Incident(Resource):
    """
        This class holds methods for single redflags
    """
    @API.doc(params={'id': 'Incident id'})
    def get(self, id):
        """
            This method retrieves an incident from the database using its id
        """
        self.model = IncidentsModel()
        redflag = self.model.get_incident_by_id(id)
        if redflag:
            return jsonify({"status": 200,
                            "data": [
                                {
                                    "redflag": redflag,
                                }
                            ],
                            "message": "Redflag successfully retrieved!"})
        return jsonify({"status": 404, "error": "Redflag not found"})

    @API.doc(params={'id': 'Incident id'})
    @jwt_required
    def put(self, id):
        """
            This method modifies an incident partially or wholly
        """
        parser.parse_args()
        self.model = IncidentsModel()

        redflag = self.model.edit_incident(id)
        if redflag:
            return jsonify({"status": 204,
                            "data": [
                                {
                                    "redflag": redflag,
                                }
                            ],
                            "message": "Redflag updated successfully!"})
        return jsonify({"status": 404, "error": "Redflag not found"})

    @jwt_required
    @API.doc(params={'id': 'Incident id'})
    def delete(self, id):
        """ 
            This method removes an incident from the db
        """
        self.model = IncidentsModel()
        redflag = self.model.delete_incident(id)
        if redflag:
            return jsonify({"status": 204, "message": "Redflag successfuly deleted"})
        return jsonify({"status": 404, "error": "Redflag not found"})


class Comment(Resource):
    """
        this class updates th description
    """
    @jwt_required
    @API.doc(params={'id': 'Incident id'})
    def patch(self, id):
        """
            This method modifies the description part of an incident.
        """
        self.model = IncidentsModel()
        comment_update = self.model.edit_incident_comment(id)
        if comment_update:
            return {"status": 204, "message": "comment successfully updated"}
        return jsonify({"status": 404, "error": "Redflag not found"})


class Location(Resource):
    """
        this class updates the location
    """
    @jwt_required
    @API.doc(params={'id': 'Incident id'})
    def patch(self, id):
        """
            This method modifies the location field of an incident
        """
        self.model = IncidentsModel()
        location_update = self.model.edit_location(id)
        if location_update:
            return {"status": 204, "message": "location successfully updated"}
        return jsonify({"status": 404, "error": "Redflag not found"})
