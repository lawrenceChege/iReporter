""" This is the base class for all the tests"""

import unittest
import datetime
from unittest import TestCase
from flask import current_app
from app import create_app


class BaseTestCase(TestCase):
    """
        This class allows for dynamic creation of the database and 
        provides a blank database after every scenario
    """

    def setUp(self):
        """
            Setup the flask app for testing. 
            It initializes the app and app context.
        """
        _app = create_app("testing")

        self.app = _app.test_client()
        self.app_context = _app.app_context()
        self.app_context.push()

        self.red_flag = {
            "createdOn": str(datetime.datetime.now()),
            "createdBy": "carolmobic",
            "type": "RedFlag",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "status": "pending",
            "Images": "[Image, Image]",
            "Videos": "[Image, Image]",
            "comment": "falling  building"
        }

        self.update_redflag = {
            "createdOn": str(datetime.datetime.now()),
            "createdBy": "carolmobic",
            "type": "RedFlag",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "status": "pending",
            "Images": "[Image, Image]",
            "Videos": "[Image, Image]",
            "comment": "falling construction building"
        }
        self.redflag_no_title = {
            "createdOn": str(datetime.datetime.now()),
            "createdBy": "carolmobic",
            "type": "RedFlag",
            "title": "",
            "location": "37.12N, 3.7E",
            "status": "pending",
            "Images": "[Image, Image]",
            "Videos": "[Image, Image]",
            "comment": "falling construction building"
        }
        self.redflag_no_comment = {
            "createdOn": str(datetime.datetime.now()),
            "createdBy": "carolmobic",
            "type": "RedFlag",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "status": "pending",
            "Images": "[Image, Image]",
            "Videos": "[Image, Image]",
            "comment": ""
        }
        self.redflag_invalid_title = {
            "createdOn": str(datetime.datetime.now()),
            "createdBy": "carolmobic",
            "type": 12345,
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "status": "pending",
            "Images": "[Image, Image]",
            "Videos": "[Image, Image]",
            "comment": "falling construction building"
        }
        self.status_Resolved = {
            "status": "Resolved"
        }
        self.status_Rejected = {
            "status": "Rejected"
        }
        self.person = {
            "id": 1,
            "firstname": "carol",
            "lastname": "mumbi",
            "email": "carolmumbi@gmail.com",
            "phoneNumber": "0708123123",
            "username": "carolmobic",
            "registered": "26/11/2018",
            "isAdmin": False,
        }
        self.person_no_username = {
            "email": "bluish@gmail.com",
            "password": "maembembili"
        }
        self.person_no_email = {
            "username": "lawrence",
            "password": "maembembili"
        }
        self.person_no_password = {
            "username": "lawrence",
            "email": "mbuchez8@gmail.com",
        }
        self.person_invalid_email = {
            "username": "lawrence",
            "email": "mbuchez.com",
            "password": "maembembili"
        }
        self.person_existing_user = {
            "id": 1,
            "firstname": "carol",
            "lastname": "mumbi",
            "email": "carolmumbi@gmail.com",
            "phoneNumber": "0708123123",
            "username": "carolmobic",
            "registered": 26/11/2018,
            "isAdmin": False,
        }

        self.correct_login = {"username": "carolmumbi",
                              "password": "liquids23"}
        self.wrong_login = {"username": "lawrence",
                            "password": "mistubishi"}
        self.no_username = {"username": "",
                            "password": "maembembili"}
        self.no_password = {"username": "lawrence",
                            "password": ""}
        self.admin = {
            "id": 1,
            "firstname": "carol",
            "lastname": "mumbi",
            "email": "carolmumbi@gmail.com",
            "phoneNumber": "0708123123",
            "username": "carolmobic",
            "registered": "26/11/2018",
            "isAdmin": False,
        }

        self.admin_correct = {"username": "admin",
                              "password": "admn1234"}
        self.admin_wrong = {"username": "lawrence",
                            "password": "mimi"}

    def test_app(self):
        """
            This method tests if an app context exists
        """
        self.assertFalse(current_app is None)

    def test_app_config(self):
        """
            This method tests if the app environment is set to testing
        """
        self.assertTrue(current_app.config['TESTING'])

    def tearDown(self):
        """
            This method is called if setUp() succeeds.
            It destroys the app context.
        """
        self.app_context.pop()


if __name__ == '__main__':
    unittest.main()
