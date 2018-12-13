"""
    This module handles the models for incidents
"""
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
import datetime
REDFLAGS = []


class IncidentsModel():
    """
        This class handles data for the redflags views
    """

    def get_all_incidents(self):
        """
            This method returns all the posted incidents
        """
        return REDFLAGS

    def post_incident(self):
        """
            This method saves an incident to the database
        """
        args = request.get_json()
        RedFlag = [
            REDFLAG for REDFLAG in REDFLAGS if REDFLAG['description'] == args["description"]]
        if len(RedFlag) == 0:
            REDFLAG = {
                "redflag_id": len(REDFLAGS)+1,
                "createdOn": str(datetime.datetime.now()),
                "modifiedOn": str(datetime.datetime.now()),
                "createdBy": str(self.current_user()),
                "type": args.get("type"),
                "title": args.get("title"),
                "images": args.get("images"),
                "video": args.get("video"),
                "location": args.get("location"),
                "status": "pending",
                "description": args.get("description")
            }
            REDFLAGS.append(REDFLAG)
            return REDFLAG
        return None

    def get_incident_by_id(self, id):
        """
            This method retrieves an incident by id from the database.
            It takes the id of the incident as parameter and
            It returns the incident as a result
        """
        REDFLAG = [REDFLAG for REDFLAG in REDFLAGS if REDFLAG['redflag_id'] == id]
        if len(REDFLAG) == 0:
            return None
        else:
            return REDFLAG

    def edit_incident(self, id):
        """
            This method can modify one or all the fields of an incident
            It takes the id of the incident as the parameter and,
            It returns the updated incident as a result.
        """
        REDFLAG = self.get_incident_by_id(id)
        if REDFLAG:
            REDFLAG[0]["title"] = request.json.get("title")
            REDFLAG[0]["type"] = request.json.get("type")
            REDFLAG[0]["modifiedOn"] = str(datetime.datetime.now())
            REDFLAG[0]["images"] = request.json.get("images")
            REDFLAG[0]["video"] = request.json.get("video")
            REDFLAG[0]["location"] = request.json.get("location")
            REDFLAG[0]["description"] = request.json.get("description")
            return REDFLAG
        else:
            return None

    def delete_incident(self, id):
        """
            This method removes an incident by id from the database.
            It takes an id of the incident as parameter and,
            It returns the list of incidents.
        """
        REDFLAG = self.get_incident_by_id(id)
        if REDFLAG:
            REDFLAGS.remove(REDFLAG[0])
            return REDFLAGS
        else:
            return None

    def edit_incident_comment(self, id):
        """
            This method modifies the description field of an incident.
            It takes an id as parameter and,
            It returns The updated incident as a result.
        """
        REDFLAG = self.get_incident_by_id(id)
        if len(REDFLAG) != 0:
            REDFLAG[0]["description"] = request.json.get("description")
            return REDFLAG
        return None

    def edit_location(self, id):
        """
            This method modifies the location field of an incident.
            Params: id.
            Return self.
        """
        REDFLAG = self.get_incident_by_id(id)
        if len(REDFLAG) != 0:
            REDFLAG[0]["location"] = request.json.get("location")
            return REDFLAG
        return None

    def upload_image(self, id):
        """
            This method posts an image or images to the database
        """
        pass

    def upload_video(self, id):
        """
            This method posts a video or videos to the database.
        """
        pass

    def current_user(self):
        """
            This method gets the logged in user from jwt token.
            It returns the username.
        """
        user = get_jwt_identity()
        return user
