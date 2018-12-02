""" These module deals with redflag methods and routes"""
import datetime
from flask_restplus import Resource
from flask import request, jsonify
from app.api.v1.models.redflags import RedflagsModel


class RedFlags(Resource):
    """
        This class has methods for posting redflags and getting all redflags posted
    """

    def post(self):
        self.model = RedflagsModel()
        new_redflag = self.model.post_redflag()
        if new_redflag:
            return jsonify({"status": 201, "data":[{
                                "RedFlag":new_redflag,
                            }],
                            "message": "Redflag posted successfully!"})
        return jsonify({"status": 400, "message": "Redflag already exists"})

    def get(self):
        self.model = RedflagsModel()
        redflags = RedflagsModel().get_all_redflags()
        return  jsonify({"status": 200, 
                        "data":[{
                            "RedFlags":redflags,
                        }],
                        "message": "All redflags found successfully"})


class RedFlag(Resource):
    """
        This class holds methods for single redflags
    """

    def get(self, id):
        self.model = RedflagsModel()
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

    def put(self, id):
        self.model = RedflagsModel()
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

    def delete(self, id):
        self.model = RedflagsModel()
        redflag = self.model.delete_redflag(id)
        if redflag:
            return jsonify({"status":204, "message":"Redflag successfuly deleted"})   
        return jsonify({"status": 404, "message": "Redflag not found"})

class Comment(Resource):
    def patch(self, id):
        self.model = RedflagsModel()
        comment_update = self.model.edit_comment(id)
        if comment_update:
            return {"status": 204, "message": "comment successfully updated"}
        return jsonify ({"status": 404, "message": "Redflag not found"})

class Location(Resource):
    def patch(self, id):
        self.model = RedflagsModel()
        location_update = self.model.edit_location(id)
        if location_update:
            return {"status": 204, "message": "location successfully updated"}
        return jsonify ({"status": 404, "message": "Redflag not found"})
