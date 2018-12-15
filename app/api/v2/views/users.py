"""
    This module holds the views for the users
"""
from flask_restplus import Resource, reqparse, Api
from flask import request, Flask, jsonify
from app.api.v2.models.users import UserModel
from app.api.v2.validators.validators import Validate


class Users(Resource):
    """
        This class defines methods for getting all users and signing up
    """

    def post(self):
        """
            This method registers a user to the database.
        """

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
                            required = True,
                            help="Email field is required.")
        parser.add_argument("firstname",
                            type=str,
                            help="Firstname field is optional.")
        parser.add_argument("lastname",
                            type=str,
                            help="Lastname field is optional.")
        parser.add_argument("phoneNumber",
                            type=int,
                            required = True,
                            help="Phone number is required")

        args = parser.parse_args()
        users = UserModel(**args)
        Valid = Validate()
        username = args.get('username').strip()
        email    = args.get('email').strip()
        password = args.get('password').strip()
        phoneNumber = str(args.get('phoneNumber')).strip()
        if not request.json:
            return {'status': 400,"error" : "check your request type"},400
        if not email or not Valid.valid_string(username) or not bool(username) :
            return {'status': 400,"error" : "Username is invalid or empty"}, 400
        if not Valid.check_phone(phoneNumber):
            return {'status': 400, 'error': 'phone number is invalid, start at [7] like 712345678'},400
        if not Valid.valid_email(email) or not bool(email):
            return {'status': 400,"error" : "Email is invalid or empty!"}, 400
        if not Valid.valid_password(password) or not bool(password):
            return {'status': 400,
            "error" : "Passord is should contain atleast 8 characters, a letter, a number and a special character"}, 400

        if users.find_by_username(username):
            return {"status": 400,  "error": "Username already in use." }, 400
        if users.find_by_email(email):
            return {"status": 400, "error": "Email already in use."}, 400


        if users.save_to_db():
            return {"status": 201,
                    "data": [
                        {
                            "id" : users.find_user_id(username)
                        }],
                        "message": 'User created Succesfully.'
                    }, 201
        return {"status":500, "error": "Oops! something went Wrong!"},500


class User(Resource):
    """
        This class defines mthods for login in
    """

    def post(self):
        """
            This method logs in the user
        """

        parser = reqparse.RequestParser(bundle_errors=True)

        parser.add_argument("username",
                            type=str,
                            required=True,
                            help="Username field is required.")
        parser.add_argument("password",
                            type=str,
                            required=True,
                            help="Password field is required.")

        args = parser.parse_args()
        users = UserModel(**args)
        Valid = Validate()

        username = args.get('username').strip()
        password = args.get('password').strip()

        if not request.json:
            return jsonify({"error" : "check your request type"})

        if not Valid.valid_string(username) or not bool(username) :
            return {"error" : "Username is invalid or empty"}, 400

        if not Valid.valid_password(password) or not bool(password):
            return {
                "error" : "Passord is should contain atleast 8 characters, a letter, a number and a special character"}, 400

        if not users.find_by_username(username):
            return {"status": 404, "error": "user not found"}, 404
        if not users.check_password_match(username, password):
            return {"status": 401, "error": "wrong credntials!"}, 401
        user_id = users.find_user_id(username)
        token = users.login_user(username)
        if token:
            return {"status": 200,
                        "data": [{
                            "id": user_id,
                            "token": "Bearer"+" "+ token
                        }],
                        "message": "successful"}, 201
        return {"status":500, "error": "Oops! something went Wrong!"},500
