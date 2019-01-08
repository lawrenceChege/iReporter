""" These module deals with redflag methods and routes"""
import datetime
from flask_restplus import Resource, reqparse, Api
from flask import request, jsonify,Flask
from flask_jwt_extended import jwt_required
from app.api.v2.models.incidents import IncidentsModel
from app.api.v2.models.users import UserModel
from app.api.v2.validators.validators import Validate


class Incidents(Resource):
    """
        This class has methods for posting redflags and getting all redflags posted
    """

    @jwt_required
    def post(self):
        """
            This method  posts an incident to the databse
        """
        parser = reqparse.RequestParser(bundle_errors=True)

        parser.add_argument("title",
                            type=str,
                            required=True,
                            help="title field is required.")
        parser.add_argument("comment",
                            type=str,
                            required=True,
                            help="comment field is required.")
        parser.add_argument("record_type",
                            type=str,
                            required=True,
                            help="Type field is required.")
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
        args = parser.parse_args()

        record_type = args.get("record_type")
        title = args.get("title")
        images = args.get("images")
        video = args.get("video")
        location = args.get("location")
        comment  = args.get("comment")
        self.model = IncidentsModel(record_type=record_type,location=location,
                images=images, video=video, title=title, comment=comment,)

        if not request.json:
            return jsonify({"error" : "check your request type"})

        if not Valid.valid_string(title) or not bool(title.strip()) :
            return {"error" : "Title is invalid or empty"}, 400

        if not Valid.valid_string(images) :
            return {"error" : "Images link is invalid"}, 400

        if not Valid.valid_string(video):
            return {"error" : "Video link is invalid"}, 400

        if not Valid.valid_string(location):
            return {"error" : "location input  is invalid"}, 400

        if not Valid.valid_string(comment) or not bool(comment.strip()) :
            return {"error" : "description is invalid or empty"}, 400

        if not Valid.valid_string(record_type) or not bool(record_type.strip()) :
            return {"error" : "Type is invalid or empty"}, 400
        
        record = Valid.check_record_type(record_type)
        if record:
            return {'error': record + ' is not a valid record_type.Use redflag or intervention'},400


        if self.model.find_incident_by_comment(comment):
            return {"status": 400, "error": "Incident already exists"}, 400

        if self.model.post_incident():
            return {"status": 201, "data": [{
                "incident_id": self.model.find_incident_id(comment),
            }],
                "message": "Created incident successfully!"}, 201

    def get(self):
        """
            This method retrives all the posted incidents from the database
        """
        self.model = IncidentsModel()
        if self.model.get_all_incidents():
            incidents = self.model.get_all_incidents()
            return {"status": 200,
                            "data": [{
                                "Incidents": incidents
                            }],
                            "message": "All incidents found successfully"}, 200
        return {"status": 404,"message": 'No incidents found'},404



class Incident(Resource):
    """
        This class holds methods for single incidents
    """
    def get(self, incident_id):
        """
            This method retrieves an incident from the database using its id
        """
        self.model = IncidentsModel()
        incident = self.model.get_incident_by_id(incident_id)
        if not incident:
            return {"status": 404, "error": "Incident not found"}, 404
        return {"status": 200,
                        "data": [
                            {
                                "incident": incident,
                            }
                        ],
                        "message": "Incident successfully retrieved!"}, 200

    @jwt_required
    def put(self, incident_id):
        """
            This method modifies an incident partially or wholly
        """
        parser = reqparse.RequestParser(bundle_errors=True)

        parser.add_argument("title",
                            type=str,
                            required=True,
                            help="title field is required.")
        parser.add_argument("comment",
                            type=str,
                            required=True,
                            help="comment field is required.")
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
        title = args.get("title")
        images = args.get("images")
        video = args.get("video")
        location = args.get("location")
        comment = args.get("comment")
        if not request.json:
            return {"error" : "check your request type"}, 400

        if not Valid.valid_string(title) or not bool(title.strip()):
            return {"error" : "Title is invalid or empty"}, 400

        if not Valid.valid_string(images) or not bool(images):
            return {"error" : "Images link is invalid"}, 400

        if not Valid.valid_string(video)or not bool(video) :
            return {"error" : "Video link is invalid"}, 400

        if not Valid.valid_string(location) or not bool(location):
            return {"error" : "location input  is invalid"}, 400

        if not Valid.valid_string(comment) or not bool(comment.strip()) :
            return {"error" : "comment is invalid or empty"}, 400

        incident = self.model.get_incident_by_id(incident_id)
        if not incident:
            return {"status": 404, "error": "Incindent not found"}, 404
        
        createdby = incident.get('createdby')        
        user = self.model.current_user()
        if user != createdby:
            return {'status': 403,"error": "This action is forbidden.",
            'message': ' You are trying to modify someone else post'}
        
        if not self.model.check_incident_status(incident_id):
            return {'status': 403,"error": "This action is forbidden"}


        if self.model.edit_incident(location, images, video, title, comment, incident_id):
            return {"status": 200,
                            "data": [
                                {
                                    "incident": incident_id,
                                }
                            ],
                            "message": "Incident updated successfully!"},200
    @jwt_required
    def delete(self, incident_id):
        """
            This method removes an incident from the db
        """
        self.model = IncidentsModel()
        incident = self.model.get_incident_by_id(incident_id)
        if not incident:
            return {"status": 404, "error": "Incident not found"}, 404

        createdby = incident.get('createdby')        
        user = self.model.current_user()
        
        if not self.model.check_incident_status(incident_id):
            return {'status': 403,"error": "This action is forbidden."}
        if user != createdby:
            return {'status': 403,"error": "This action is forbidden.",
            'message': ' You are trying to delete someone else post'}

        if self.model.delete_incident(incident_id):
            return {"status": 200,
                            "data": [
                                {
                                    "incident": incident_id,
                                }
                            ],
                             "message": "Incident successfuly deleted"}, 200


class Comment(Resource):
    """
        this class updates th comment
    """
    @jwt_required
    def patch(self, incident_id):
        """
            This method modifies the comment part of an incident.
        """
        parser = reqparse.RequestParser(bundle_errors=True)

        parser.add_argument("comment",
                            type=str,
                            required=True,
                            help="comment field is required.")
        Valid = Validate()
        self.model = IncidentsModel()
        args = parser.parse_args()
        comment = args.get("comment")

        if not Valid.valid_string(comment) or not bool(comment.strip()):
            return {"error" : "Comment is invalid or empty"}, 400

        incident = self.model.get_incident_by_id(incident_id)
        if not incident:
            return {"status": 404, "error": "Incindent not found"}, 404
        
        createdby = incident.get('createdby')        
        user = self.model.current_user()
        if user != createdby:
            return {'status': 403,"error": "This action is forbidden.",
            'message': ' You are trying to modify someone else post'}
        
        if not self.model.check_incident_status(incident_id):
            return {'status': 403,"error": "This action is forbidden"}

        if self.model.edit_incident_comment(comment, incident_id):
            incident_id = self.model.find_incident_id(comment)
            return {"status": 200,
                    "data": [
                        {"id": incident_id}
                    ],
                    "message": "comment successfully updated"}, 200




class Location(Resource):
    """
        this class updates the location
    """
    @jwt_required
    def patch(self, incident_id):
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
        location = args.get("location")

        if not Valid.valid_string(location.strip()) and not bool(location.strip()):
            return {"error" : "location input  is invalid"}, 400
        if not Valid.check_loaction(location):
            return {'status': 400, 'error': 'location input format should be a valid lat n long pair'},400
        incident = self.model.get_incident_by_id(incident_id)
        if not incident:
            return {"status": 404, "error": "Incindent not found"}, 404
        createdby = incident.get('createdby')
        user = self.model.current_user()
        if user != createdby:
            return {'status': 403,"error": "This action is forbidden",
            'message': ' You are trying to modify someone else post'}

        if not self.model.check_incident_status(incident_id):
            return {'status': 403,"error": "This action is forbidden"}
        if self.model.edit_location(location, incident_id):
            return {"status": 200,
                            "data": [
                                {
                                    "incident": incident_id,
                                }
                            ],
                            "message": "location successfully updated"}, 200


class Status(Resource):
    """
        this class updates the status
    """
    @jwt_required
    def patch(self, incident_id):
        """
            This method modifies the status field of an incident
        """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("status",
                            type=str,
                            required = True,
                            help="status field is optional.")
        Valid = Validate()
        self.model = IncidentsModel()
        self.user = UserModel()
        args = parser.parse_args()
        status = args.get("status")
        user = self.model.current_user()
        if user != 1 :
            return {'status': 403, 'error': 'you do not have permission to do that!'},403
        if not Valid.valid_string(status.strip()):
            return {"error" : "status input  is invalid"}, 400
        state = Valid.check_status(status)
        if state:
            return {'status': 400,
            'error': state + ' is not a valid status. Use under-investigation, resolved, rejected or pending'},400
        incident = self.model.get_incident_by_id(incident_id)
        createdby = incident.get('createdby')
        old_status = incident.get('status')
        print(status, old_status)
        if not incident:
            return {"status": 404, "error": "Incindent not found"}, 404
        if not self.model.check_status_match(status, old_status):
            return {'status': 400, 'error': 'status already updated to '+ status}, 400
        if not self.model.check_status_investigation(status, old_status):
            return {'status':400, 'error': 'only incidents under investigation can be marked as resolved'}, 400
        if not self.model.check_status_resolved(status, old_status):
            return {'status':400, 'error': 'status marked as resolved can only be changed to under-investigation'}, 400
        if self.model.edit_status(status, incident_id):
            user = self.user.find_user_by_id(createdby)
            email = user.get('email')
            username = user.get('username')
            phone = str(user.get('phonenumber'))
            self.model.send_email(incident_id, username, email, status)
            self.model.send_sms(incident_id, username, phone, status)
            return {"status": 200,
                            "data": [
                                {
                                    "incident": incident_id,
                                }
                            ],
                            "message": "status successfully updated"}, 200

class Filter_by_recordtype(Resource):
    """
        Filter records by by either redflags or incidents
    """
    def get(self, record_type):
        """
            Gets all incidents by the specified record type
        """
        self.model = IncidentsModel()
        incidents = self.model.find_by_recordtype(record_type)
        if not incidents:
            return {
                "status": 404,
                "error":"No "+ record_type + "s Found"
            },404
        return {
            "status":200,
            "data":[
                {' '+ record_type +'': incidents}
            ],
            "message":"All "+ record_type +"s found successfully"
        }

class MyIncidents(Resource):
    """
        Gets current user's Incidents
    """
    @jwt_required
    def get(self):
        """
            Fetch current users incidents
        """
        self.model = IncidentsModel()
        incidents = self.model.find_my_incidents()
        if not incidents:
            return {
                "status": 404,
                "error": "No personal incidents found"
            },404
        return {
            "status" :200,
            "data": [{
                "incidents": incidents
            }],
            "message": "All my incidents found"
        }



