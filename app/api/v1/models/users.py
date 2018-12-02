from flask_restplus import reqparse
from flask import request
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

USERS = []

class UserModel():
    id = 1
    def __init__(self, firstname=None, 
                lastname=None, email=None, phoneNumber=None, username=None, password=None):
        self.id = UserModel.id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = self.generate_pass_hash(password)
        self.phoneNumber = phoneNumber
        self.username = username
        self.created_on = datetime.datetime.now()
        self.db = USERS

        UserModel.id += 1

    @staticmethod
    def generate_pass_hash(password):
        """
        encrypt password
        """

        private_key = generate_password_hash(password)
        return private_key
    
    def check_password_match(self, password):
        """
        Check if pass match

        :param :password: password
        return: Boolean
        """
        match = check_password_hash(self.password, password)
        return match

    def find_by_id(self, id):
        """
        Find user by id
        """
        for user in self.db:
            if user["id"] == id:
                return user
            return None

    def find_by_username(self, username):
        """
        Find user by username
        """
        user = [u.username for u in self.db if u.username == username]

        if user: 
            return user

        return None

    def save_to_db(self):
        self.db.append(self)

    def login_user(self, id):
        u = self.find_by_id(id)

        if u:
            if u["password"]== request.json["password"]:
                    return {"status": 200, "message":"successful"}
            return {"status": 401, "message": "wrong credntials!"}
        
        return {"status":404, "message": "user not found"}
               