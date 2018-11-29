from flask_restplus import Resource 
from flask import request

class Users(Resource):
    """
        This class defines methods for getting all users and signing up
    """
    def post(self):
        user_signup = Helper().signup_user()
        return user

class User(Resource):
    """
        This class defines mthods for login in
    """
    def post(self, user_id):
        user_login = Helper().login_user(user_id)
        return user_login