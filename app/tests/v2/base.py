""" This is the base class for all the tests"""

import unittest
from unittest import TestCase
from flask import current_app
from app import create_app
from migrations import DbModel


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
        APP = create_app("testing")
        self.app = APP.test_client()
        self.app_context = APP.app_context()
        self.app_context.push()
        with APP.app_context():
            db = DbModel()
            db.init_db(APP)
            db.drop_tables('incidents')
            db.drop_tables('users')
            db.create_tables()
        self.token = 0

        self.red_flag = {
            "record_type": "RedFlag",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "video": "[Image, Image]",
            "comment": "falling  building"
        }
        self.redflag_location = {
            "location": "37.12N, 3.7E"
        }
        self.redflag_comment = {
            "comment": "something nice"
        }
        self.red_flag2 = {
            "record_type": "RedFlag",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "video": "[Image, Image]",
            "comment": "falling  building is here"
        }
        self.red_flag3 = ()


        self.update_redflag = {
            "record_type": "RedFlag",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "video": "[Image, Image]",
            "comment": "falling construction building"
        }
        self.redflag_no_title = {
            "record_type": "RedFlag",
            "title": "",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "video": "[Image, Image]",
            "comment": "falling construction building"
        }
        self.redflag_invalid_type = {
            "record_type": "",
            "title": "this is nice",
            "location": "37.12N, 3.7E",
            "images": 'jjj',
            "video": "[Image, Image]",
            "comment": "falling constructions center"
        }
        self.redflag_invalid_image = {
            "record_type": "RedFlag",
            "title": "this is nice",
            "location": "37.12N, 3.7E",
            "video": "[Image, Image]",
            "comment": "falling constructions center"
        }
        self.redflag_invalid_location = {
            "record_type": "RedFlag",
            "title": "this is nice",
            "images": "37.12N, 3.7E",
            "video": "[Image, Image]",
            "comment": "falling constructions center"
        }
        self.redflag_no_comment = {
            "record_type": "RedFlag",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "video": "[Image, Image]",
            "comment": ""
        }
       
        self.redflag_invalid_video = {
            "record_type": "12345",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "comment": "falling construction kapanga building"
        }
        self.status_Resolved = {
            "status": "Resolved"
        }
        self.status_Rejected = {
            "status": "Rejected"
        }
        self.person = {
            "firstname": "carol",
            "lastname": "mumbi",
            "email": "carolmumbi@gmail.com",
            "phoneNumber": "0708123123",
            "username": "carolmobic",
            "password": "mae12#embiliA"
        }
        self.person1 = {
            "firstname": "mwaniki",
            "lastname": "mumbi",
            "email": "carolmumbi@gmail.com",
            "phoneNumber": "0708123123",
            "username": "carolnice",
            "password": "mae12#embiliA"
        }
        self.person_no_username = {
            "email": "bluish@gmail.com",
            "password": "mae12#embili"
        }
        self.person_no_email = {
            "username": "lawrence",
            "password": "mae12#embili"
        }
        self.person_no_password = {
            "username": "lawrence",
            "email": "mbuchez8@gmail.com",
        }
        self.person_invalid_email = {
            "username": "lawrence",
            "email": "mbuchez.com",
            "password": "mae12#embili"
        }
        self.person_invalid_username = {
            "username": "",
            "email": "mbuchez@gmail.com",
            "password": "mae12#embili"
        }
        self.person_invalid_password = {
            "username": "mama yao",
            "email": "mbuchez@gmail.com",
            "password": "maembe"
        }
        self.person_existing_user = {
            "firstname": "carolol",
            "lastname": "mumbi",
            "email": "carolmumbi@gmail.com",
            "phoneNumber": "0708123123",
            "username": "carolmobic",
            "password": "aswdeAWSE$WE"
        }

        self.correct_login = {
            "username": "carolmobic",
            "password": "mae12#embiliA"
            }
        self.correct_login1 = {
            "username": "carolmobic",
            "password": "aswdeAWSE$WE"
            }

        self.wrong_login = {"username": "carolmoboc",
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
            "registered": "26/11/2018"
        }

        self.admin_correct = {"username": "admin",
                              "password": "admn1234"}
        self.admin_wrong = {"username": "lawrence",
                            "password": "mimi"}

    def tearDown(self):
        """
            This method is called if setUp() succeeds.
            It destroys the app context.
        """
        pass


if __name__ == '__main__':
    unittest.main()
