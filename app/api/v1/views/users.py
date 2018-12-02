from flask_restplus import Resource,reqparse
from flask import request
from app.api.v1.models.users import UserModel 
import json

parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument("username",
                    type=str,
                    required=True,
                    help="Username field is required.")
parser.add_argument("password",
                    type=str,
                    required=True,
                    help="password field is required.")

class Users(Resource):
    """
        This class defines methods for getting all users and signing up
    """
    def post(self):

        data = parser.parse_args()
        # Validation
        # valid = validtion(data)

        # if not valid["isValid"]:
        #     return {
        #         "status": 400,
        #         "data": json.dumps(valid["errors"])
        #     }           
        user = UserModel(**data)

        if user.find_by_username():
            return {"status": 400,
                    "data":[
                        {
                            "message": "Username already in use."
                        }
                    ]}
        user.save_to_db()
        return {"status": 201,
                "data":[
                    {
                        "id": user.id,
                        "message": 'User created Succesfully.'
                    }
                ]}

class User(Resource):
    """
        This class defines mthods for login in
    """
    def post(self):
        data = parser.parse_args()
        user = UserModel(**data)
        user_login = user.login_user()
        return user_login

