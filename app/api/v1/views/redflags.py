""" These module deals with redflag methods and routes"""
import datetime
from flask_restplus import Resource
from flask import request
from app.api.v1.models.redflags import RedflagsModel


class RedFlags(Resource):
    """
        This class has methods for posting redflags and getting all redflags posted
    """
    def __init__(self):
        self.model = RedflagsModel()

    def post(self):
        new_redflag = self.model.post_redflag()
        return new_redflag

    def get(self):
        redflags = self.model.get_all_redflags()
        return redflags


class RedFlag(Resource):
    """
        This class holds methods for single redflags
    """
    def __init__(self):
        self.model = RedflagsModel()

    def get(self, id):
        get_specific = self.model.get_redflag(id)
        return get_specific

    def put(self, id):
        edit_one = self.model.edit_redflag(id)
        return edit_one

    def delete(self, id):
        remove_redflag = self.model.delete_redflag(id)
        return remove_redflag

    def patch(self, id):
        comment_update = self.model.edit_comment(id)
        return comment_update
