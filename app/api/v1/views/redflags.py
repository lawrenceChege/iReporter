""" These module deals with redflag methods and routes"""
import datetime
from flask-restplus import Resource
from flask import request
from app.api.v1.models.redflags import Helper

class RedFlags(Resource):
    """
        This class has methods for posting redflags and getting all redflags posted
    """
    def post(self):
        new_redflag = Helper().post_redflag()
        return new_redflag

    def get(self):
        redflags = Helper().get_all()
        return redflags 

class RedFlag(Resource):
    """
        This class holds methods for single redflags
    """
    def get(self, redflag_id):
        get_specific = Helper().get_redflag()
        return get_specific
    def put(self, redflag_id):
        edit_one = Helper().edit_redflag()
        return edit_one
    def delete(self, redflag):
        remove_redflag = Helper().delete_redflag()
        return remove_redflag

