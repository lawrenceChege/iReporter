""" These module deals with redflag methods and routes"""
import datetime
from flask-restplus import Resource, reqparse
from flask import request

REDFLAGS = []

class RedFlags(Resource):
    """
        This class has methods for posting redflags and getting all redflags posted
    """
    def get(self):
        pass

    def post(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str, help=" the title of the record")
        self.parser.add_argument("location", type=str, help=" the location of the record")
        self.parser.add_argument("comment", type=str, help="Body is required")
        args = self.parser.parse_args()   


        REDFLAG = {
                "id": len(REDFLAGS)+1,
                "createdOn" : datetime.now,  
                "createdBy" : "carolmobic",
                "type" : "RedFlag",
                "title": args["title"],
                "location" : args["location"],
                "status": "pending",
                "comment" : args["comment"]
            }
        REDFLAGS.append(REDFLAG)
        return REDFLAGS,201
        
