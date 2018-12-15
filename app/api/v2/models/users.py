"""
    This module holds the Model for the Users
"""
import time
import psycopg2
from flask import request
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from migrations import DbModel




class UserModel(DbModel):
    """
        This class manages the data for the users
    """

    def __init__(self, firstname=None, othernames=None, isAdmin=False,
                 lastname=None, email=None, phoneNumber=None, username=None, password=None):
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.password = password
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = time.strftime('%a, %d %b %Y, %I:%M:%S %p')
        self.isAdmin = isAdmin
        self.Admin = self.is_admin()


    def generate_pass_hash(self):
        """
        encrypt password
        """

        private_key = generate_password_hash(request.json.get("password"))
        self.password = private_key
        return self.password

    def check_password_match(self, username, password):
        """
        Check if pass match

        :param :password: password
        return: Boolean
        """
        self.password = self.get_password(username).get('btrim')
        match = check_password_hash(self.password, password)
        return match

    def generate_jwt_token(self, username):
        self.user_id = self.find_user_id(username)
        token = create_access_token(identity=self.user_id)
        return token

    def get_password(self, username):
        """ gets hash password from db """
        try:
            self.cur.execute(
                "SELECT TRIM(password) FROM users WHERE username=%s", (username,)
                )
            password = self.findOne()
            return password
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def find_user_id(self, username):
        """
        Find user  id
        """
        try:
            self.cur.execute(
                "SELECT user_id FROM users WHERE username=%s", (username,)
                )
            user_id = self.findOne()
            id = user_id.get('user_id')
            return id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None
    def find_user_by_id(self, user):
        """
        Find user email and phoneNumber
        """
        try:
            self.cur.execute(
                "SELECT * FROM users WHERE user_id=%s", (user,)
                )
            self.user = self.findOne()
            return self.user
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None
    
    def find_user_role(self, user):
        """
        Find user role
        """
        try:
            self.cur.execute(
                "SELECT isAdmin FROM users WHERE user_id=%s", (user,)
                )
            user_role = self.findOne()
            print(user_role)
            isAdmin = user_role.get('isAdmin')
            return isAdmin
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def find_by_email(self,email):
        """
        Find user by email
        """
        try:
            self.cur.execute(
                "SELECT TRIM(email) FROM users WHERE email=%s", (email,)
                )
            email = self.findOne()
            return email
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def find_by_username(self, username):
        """
        Find user by username
        """
        try:
            self.cur.execute(
                "SELECT username FROM users WHERE username=%s", (username,)
                )
            username = self.findOne()
            return username
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def save_to_db(self):
        """
            This method saves the user to the database.
        """
        self.generate_pass_hash()
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

    def login_user(self, username):
        """
            This method logs in the user.
            It takes username and password as parameters and
            It returns jwt token
        """
        token = self.generate_jwt_token(username)
        return token

    def is_admin(self):
        try:
            user = self.find_by_username('Admin')
            if user:
                self.user = user
            else:
                data = ('Administrator', 'One', 'main', 'Admin', 'admin@gmail.com',
                        708686842, generate_password_hash('Admin$123G'), time.strftime('%a, %d %b %Y, %I:%M:%S %p'), True, )
                self.cur.execute(
                    """
                        INSERT INTO users (firstname, lastname, othernames, username, email, phoneNumber, password, registered, isAdmin)
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """, data
                )
                self.commit()
                return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('could not save to db')
