from flask_restplus import Resource 
from flask import request

class Users(Resource):
    """
        This class defines methods for getting all users
    """
    def post(self):
        user = Helper().post_user()
        return user