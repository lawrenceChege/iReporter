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
        post_redflag = Helper().new_redflag()
        return post_redflag

    def get(self):
        redflags = Helper().get_all()

        return redflags 

class RedFlag(Resource):
    """
        This class holds methods for single redflags
    """
    def get(self, redflag_id):
        get_specific = Helper().get_one()
        return get_specific

