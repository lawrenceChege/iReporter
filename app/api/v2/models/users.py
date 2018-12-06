"""
    This module holds the Model for the Users
"""
import os
import datetime
import psycopg2
from flask_restplus import reqparse
from flask import request
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from migrations import DbModel


class UserModel(DbModel):
    """
        This class manages the data for the users
    """
    id = 1

    def __init__(self, firstname=None, othernames=None, isAdmin=False, 
                 lastname=None, email=None, phoneNumber=None, username=None, password=None):
        super().__init__('main')
        self.id = UserModel.id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.password = self.generate_pass_hash()
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = datetime.datetime.now()
        self.isAdmin = isAdmin

        UserModel.id += 1

    @staticmethod
    def generate_pass_hash():
        """
        encrypt password
        """

        private_key = generate_password_hash(request.json["password"])
        return private_key

    def check_password_match(self):
        """
        Check if pass match

        :param :password: password
        return: Boolean
        """
        match = check_password_hash(self.password, request.json["password"])
        return match

    def generate_jwt_token(self):
        token = create_access_token(identity=self.username)
        return token

    def find_by_id(self, user_id):
        """
        Find user by id
        """
        try:
            self.cur.execute(
                "SELECT TRIM(user_id) FROM users WHERE user_id=%s", (user_id,)
                )
            user = self.findOne()
            return user
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def find_by_username(self, username):
        """
        Find user by username
        """
        try:
            self.cur.execute(
                "SELECT TRIM(username) FROM users WHERE username=%s", (username,))
            user = self.findOne()
            print(user)
            return user
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def save_to_db(self):
        """
            This method saves the user to the database.
        """
        try:
            data =( self.firstname, self.lastname, self.othernames, self.username, self.email, self.phoneNumber, self.password, self.registered, self.isAdmin, )
            self.cur.execute(
                """
                    INSERT INTO users (firstname, lastname, othernames, username, email, phoneNumber, password, registered, isAdmin)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, data
            )
            self.commit()
            print('success')
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('could not save to db')
            return None

    def login_user(self):
        """
            This method logs in the user.
            It takes username and password as parameters and
            It returns jwt token
        """
        if self.check_password_match():
            token = self.generate_jwt_token()
            return token
        return None
