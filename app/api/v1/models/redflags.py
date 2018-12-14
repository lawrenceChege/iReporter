"""
    This module handles the models for incidents
"""
from flask import request
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
        self.args = request.get_json()
        RedFlag = [
            REDFLAG for REDFLAG in REDFLAGS if REDFLAG['description'] == self.args["description"]]
        if len(RedFlag) == 0:
            REDFLAG = {
                "redflag_id": len(REDFLAGS)+1,
                "createdOn": str(datetime.datetime.now()),
                "modifiedOn": str(datetime.datetime.now()),
                "createdBy": str(self.current_user()),
                "type": self.args.get("type"),
                "title": self.args.get("title"),
                "images": self.args.get("images"),
                "video": self.args.get("video"),
                "location": self.args.get("location"),
                "status": "pending",
                "description": self.args.get("description")
            }
            REDFLAGS.append(REDFLAG)
            return REDFLAG
        return None

    def get_incident_by_id(self, incident_id):
        """
            This method retrieves an incident by id from the database.
            It takes the id of the incident as parameter and
            It returns the incident as a result
        """
        self.REDFLAG = [REDFLAG for REDFLAG in REDFLAGS if REDFLAG['redflag_id'] == incident_id]
        if len(self.REDFLAG) == 0:
            return None
        else:
            return self.REDFLAG

    def edit_incident(self, incident_id):
        """
            This method can modify one or all the fields of an incident
            It takes the incident_id of the incident as the parameter and,
            It returns the updated incident as a result.
        """
        self.REDFLAG = self.get_incident_by_id(incident_id)
        if self.REDFLAG:
            self.REDFLAG[0]["title"] = request.json.get("title")
            self.REDFLAG[0]["type"] = request.json.get("type")
            self.REDFLAG[0]["modifiedOn"] = str(datetime.datetime.now())
            self.REDFLAG[0]["images"] = request.json.get("images")
            self.REDFLAG[0]["video"] = request.json.get("video")
            self.REDFLAG[0]["location"] = request.json.get("location")
            self.REDFLAG[0]["description"] = request.json.get("description")
            return self.REDFLAG
        else:
            return None

    def delete_incident(self, incident_id):
        """
            This method removes an incident by incident_id from the database.
            It takes an incident_id of the incident as parameter and,
            It returns the list of incidents.
        """
        self.REDFLAG = self.get_incident_by_id(incident_id)
        if self.REDFLAG:
            REDFLAGS.remove(self.REDFLAG[0])
            return REDFLAGS
        else:
            return None

    def edit_incident_comment(self, incident_id):
        """
            This method modifies the description field of an incident.
            It takes an incident_id as parameter and,
            It returns The updated incident as a result.
        """
        self.REDFLAG = self.get_incident_by_id(incident_id)
        if len(self.REDFLAG) != 0:
            self.REDFLAG[0]["description"] = request.json.get("description")
            return self.REDFLAG
        return None

    def edit_location(self, incident_id):
        """
            This method modifies the location field of an incident.
            Params: incident_id.
            Return self.
        """
        self.REDFLAG = self.get_incident_by_id(incident_id)
        if len(self.REDFLAG) != 0:
            self.REDFLAG[0]["location"] = request.json.get("location")
            return self.REDFLAG
        return None

    def current_user(self):
        """
            This method gets the logged in user from jwt token.
            It returns the username.
        """
        self.user = get_jwt_identity()
        return self.user
