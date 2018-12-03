""" These module deals with redflag methods and routes"""
import datetime
from flask_restplus import Resource, reqparse
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.api.v1.models.redflags import IncidentsModel
from app.api.v1.validators.validators import Validate

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
    def post(self):
        
        self.validate = Validate()
        self.model = IncidentsModel()
        parser.parse_args()
        # valid = self.validate.check_redflag()
        if self.validate.check_redflag() is None:
            new_redflag = self.model.post_redflag()
            if new_redflag:
                return jsonify({"status": 201, "data":[{
                                    "RedFlag_id":new_redflag,
                                }],
                                "message": "Redflag posted successfully!"})
            return jsonify({"status": 400, "message": "Redflag already exists"})

    def get(self):
        self.model = IncidentsModel()
        redflags = self.model.get_all_redflags()
        return  jsonify({"status": 200, 
                        "data":[{
                            "RedFlags":redflags,
                        }],
                        "message": "All redflags found successfully"})


class Incident(Resource):
    """
        This class holds methods for single redflags
    """

    def get(self, id):
        self.model = IncidentsModel()
        redflag = self.model.get_redflag(id)
        if redflag:
            return jsonify({"status": 200,
                             "data":[
                                 {
                                     "redflag": redflag,
                                 }
                             ],
                             "message": "Redflag successfully retrieved!"})
        return jsonify({"status": 404, "message": "Redflag not found"})

    @jwt_required
    def put(self, id):
        
        data = parser.parse_args()
        self.model = IncidentsModel()

        redflag = self.model.edit_redflag(id)
        if redflag:
            return jsonify( {"status":204,
                              "data":[
                                 {
                                     "redflag": redflag,
                                 }
                             ],
                             "message": "Redflag updated successfully!"}) 
        return jsonify({"status": 404, "message": "Redflag not found"})

    @jwt_required
    def delete(self, id):
        self.model = IncidentsModel()
        redflag = self.model.delete_redflag(id)
        if redflag:
            return jsonify({"status":204, "message":"Redflag successfuly deleted"})   
        return jsonify({"status": 404, "message": "Redflag not found"})

class Comment(Resource):
    """
        this class updates th description
    """
    @jwt_required
    def patch(self, id):
        self.model = IncidentsModel()
        comment_update = self.model.edit_comment(id)
        if comment_update:
            return {"status": 204, "message": "comment successfully updated"}
        return jsonify ({"status": 404, "message": "Redflag not found"})

class Location(Resource):
    """
        this class updates the location
    """
    @jwt_required
    def patch(self, id):
        self.model = IncidentsModel()
        location_update = self.model.edit_location(id)
        if location_update:
            return {"status": 204, "message": "location successfully updated"}
        return jsonify ({"status": 404, "message": "Redflag not found"})
