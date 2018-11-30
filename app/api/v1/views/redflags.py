""" These module deals with redflag methods and routes"""
import datetime
from flask_restplus import Resource
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
        redflags = Helper().get_all_redflags()
        return redflags


class RedFlag(Resource):
    """
        This class holds methods for single redflags
    """

    def get(self, id):
        get_specific = Helper().get_redflag(id)
        return get_specific

    def put(self, id):
        edit_one = Helper().edit_redflag(id)
        return edit_one

    def delete(self, id):
        remove_redflag = Helper().delete_redflag(id)
        return remove_redflag

    def patch(self, id):
        comment_update = Helper().edit_comment(id)
        return comment_update
