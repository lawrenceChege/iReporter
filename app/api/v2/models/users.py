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
from migrations import connection

DATABASE_URL = os.getenv('DATABASE_URL')
USERS = []


def conn():
    try:
        print("connecting to db...\n")
        try:
            conn = connection(DATABASE_URL)
            print('connected to db\n')
            return conn
        except:
            conn = psycopg2.connect(
                'postgresql://localhost/ireporter?user=postgres&password=12345678')
            print('connected to db\n')
            return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('error connecting to db\n')


class UserModel():
    """
        This class manages the data for the users
    """
    id = 1

    def __init__(self, firstname=None,
                 lastname=None, email=None, phoneNumber=None, username=None, password=None):
        self.id = UserModel.id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = self.generate_pass_hash()
        self.phoneNumber = phoneNumber
        self.username = username
        self.created_on = datetime.datetime.now()
        self.db = USERS
        self.conn = conn()
        self.cur = self.conn.cursor()

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
                "SELECT TRIM(user_id) FROM users WHERE user_id=%s", (user_id,))
            user = self.cur.fetchone()
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
            user = self.cur.fetchone()
            return user
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def save_to_db(self):
        """
            This method saves the user to the database.
        """
        try:
            self.cur.execute(
                """
                    INSERT INTO users (firstname, lastname, othernames, username, email, password, registered, isAdmin)
                    VALUES(%(firstname)s, %(lastname)s, %(othernames)s, %(username)s, %(email)s, %(password)s, %(registered)s, %(isAdmin)s)
                """, self
            )
            self.conn.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
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
