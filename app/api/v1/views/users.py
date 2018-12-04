"""
    This module holds the views for the users
"""
import json
from flask_restplus import Resource, reqparse, Api
from flask import request, Flask
from app.api.v1.models.users import UserModel

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument("username",
                    type=str,
                    required=True,
                    help="Username field is required.")
parser.add_argument("password",
                    type=str,
                    required=True,
                    help="Password field is required.")
parser.add_argument("email",
                    type=str,
                    help="Email field is required.")
parser.add_argument("firstname",
                    type=str,
                    help="Firstname field is optional.")
parser.add_argument("lastname",
                    type=str,
                    help="Lastname field is optional.")
parser.add_argument("phoneNumber",
                    type=int,
                    help="Phone number field is optional.")


class Users(Resource):
    """
        This class defines methods for getting all users and signing up
    """

    @api.doc(params={'firstname': 'Enter first name',
                    'lastname': 'Enter last name',
                    'email': 'Enter email',
                    'phoneNumber': 'Enter phone number',
                    'username': 'Enter a unique username',
                    'password': 'Enter password'})
    def post(self):
        """
            This method registers a user to the database.
        """

        data = parser.parse_args()
        user = UserModel(**data)

        if user.find_by_username():
            return {"status": 400,
                    "data": [
                        {
                            "message": "Username already in use."
                        }
                    ]}
        user.save_to_db()
        return {"status": 201,
                "data": [
                    {
                        "id": user.id,
                        "message": 'User created Succesfully.'
                    }
                ]}


class User(Resource):
    """
        This class defines mthods for login in
    """
    @api.doc(params={'Username': 'Enter a unique username',
                    'password': 'Enter password'})
    def post(self):
        """
            This method logs in the user
        """
        data = parser.parse_args()
        user = UserModel(**data)
        user_login = user.login_user()
        return user_login
