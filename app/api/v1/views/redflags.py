""" These module deals with redflag methods and routes"""
import datetime
from flask_restplus import Resource, reqparse, Api
from flask import request, jsonify,Flask
from flask_jwt_extended import jwt_required

from app.api.v1.models.redflags import IncidentsModel

from app.api.v1.validators.validators import Validate

app =Flask(__name__)
API = Api(app)

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

        Valid = Validate()
        self.model = IncidentsModel()
        args = parser.parse_args()
        title = args["title"].strip()
        images = args["images"].strip()
        video = args["video"].strip()
        location = args["location"].strip()
        description= args["description"].strip()
        if not request.json:
            return jsonify({"error" : "check your request type"})
        if not Valid.valid_string(title) or not bool(title) :
            return {"error" : "Title is invalid or empty"}, 400
        if not Valid.valid_string(images) :
            return {"error" : "Images link is invalid"}, 400
        if not Valid.valid_string(video):
            return {"error" : "Video link is invalid"}, 400
        if not Valid.valid_string(location):
            return {"error" : "location input  is invalid"}, 400
        if not Valid.valid_string(description) or not bool(description) :
            return {"error" : "description is invalid or empty"}, 400

        new_redflag = self.model.post_incident()
        if new_redflag:
            return {"status": 201, "data": [{
                "RedFlag_id": new_redflag,
            }],
                "message": "Redflag posted successfully!"}, 201
        return {"status": 400, "error": "Redflag already exists"}, 400

    @API.doc('List all Incidents')
    def get(self):
        """ 
            This method retrives all the posted incidents from the database
        """
        self.model = IncidentsModel()
        redflags = self.model.get_all_incidents()
        return {"status": 200,
                        "data": [{
                            "RedFlags": redflags,
                        }],
                        "message": "All redflags found successfully"}, 200


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
            return {"status": 200,
                            "data": [
                                {
                                    "redflag": redflag,
                                }
                            ],
                            "message": "Redflag successfully retrieved!"}, 200
        return {"status": 404, "error": "Redflag not found"}, 404

    @API.doc(params={'id': 'Incident id'})
    @jwt_required
    def put(self, id):
        """
            This method modifies an incident partially or wholly
        """
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
        Valid = Validate()
        self.model = IncidentsModel()
        args = parser.parse_args()
        title = args["title"].strip()
        images = args["images"].strip()
        video = args["video"].strip()
        location = args["location"].strip()
        description= args["description"].strip()
        if not request.json:
            return jsonify({"error" : "check your request type"})
        if not Valid.valid_string(title) or not bool(title):
            return {"error" : "Title is invalid or empty"}, 400
        if not Valid.valid_string(images) or not bool(images):
            return {"error" : "Images link is invalid"}, 400
        if not Valid.valid_string(video)or not bool(video) :
            return {"error" : "Video link is invalid"}, 400
        if not Valid.valid_string(location) or not bool(location):
            return {"error" : "location input  is invalid"}, 400
        if not Valid.valid_string(description) or not bool(description) :
            return {"error" : "description is invalid or empty"}, 400

        redflag = self.model.edit_incident(id)
        if redflag:
            return {"status": 200,
                            "data": [
                                {
                                    "redflag": redflag,
                                }
                            ],
                            "message": "Redflag updated successfully!"},200
        return {"status": 404, "error": "Redflag not found"},404

    @jwt_required
    @API.doc(params={'id': 'Incident id'})
    def delete(self, id):
        """ 
            This method removes an incident from the db
        """
        self.model = IncidentsModel()
        redflag = self.model.delete_incident(id)
        if redflag:
            return {"status": 200, "message": "Redflag successfuly deleted"}, 200
        return {"status": 404, "error": "Redflag not found"}, 404


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
        parser = reqparse.RequestParser(bundle_errors=True)

        parser.add_argument("description",
                            type=str,
                            required=True,
                            help="description field is required.")
        Valid = Validate()
        self.model = IncidentsModel()
        args = parser.parse_args()
        description = args["description"].strip()
        if not Valid.valid_string(description) or not bool(description) :
            return {"error" : "description is invalid or empty"}, 400

        comment_update = self.model.edit_incident_comment(id)
        if comment_update:
            return {"status": 200, "message": "comment successfully updated"}, 200
        return {"status": 404, "error": "Redflag not found"}, 404


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
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("location",
                            type=str,
                            required = True,
                            help="location field is optional.")
        Valid = Validate()
        self.model = IncidentsModel()
        args = parser.parse_args()
        location = args["location"].strip()
        if not Valid.valid_string(location):
            return {"error" : "location input  is invalid"}, 400
        location_update = self.model.edit_location(id)
        if location_update:
            return {"status": 200, "message": "location successfully updated"}, 200
        return {"status": 404, "error": "Redflag not found"}, 404    
