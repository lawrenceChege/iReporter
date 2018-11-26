""" This is the base class for all the tests"""
import unittest

class BaseTestCase(TestCase):
    """ set up configurations for the test environment"""
    @classmethod
    def setUpClass(self):
        """set up app configuration"""
        self.app = APP.test_client()
        self.app.testing = True
        self.users = [
             {
            “id” : 1, 
            “firstname” : "carol",
            “lastname” : "mumbi",
            “email” : "carolmumbi@gmail.com",
            ”phoneNumber” : "0708123123",
            “username” : "carolmobic", 
            “registered” : 26/11/2018,
            “isAdmin” : False,
            },
             {
            “id” : 2, 
            “firstname” : "lawrence",
            “lastname” : "chege",
            “email” : "laurencechege@gmail.com",
            ”phoneNumber” : "0708123123",
            “username” : "lauchege", 
            “registered” : 26/11/2018,
            “isAdmin” : False,
            },
             {
            “id” : 3, 
            “firstname” : "kenn",
            “lastname” : "hinga",
            “email” : "kenn@gmail.com",
            ”phoneNumber” : "0708123123",
            “username” : "gathee", 
            “registered” : 26/11/2018,
            “isAdmin” : False,
            }
        ]
        self.person = {
            “id” : 1, 
            “firstname” : "carol",
            “lastname” : "mumbi",
            “email” : "carolmumbi@gmail.com",
            ”phoneNumber” : "0708123123",
            “username” : "carolmobic", 
            “registered” : 26/11/2018,
            “isAdmin” : False,
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
            “id” : 1, 
            “firstname” : "carol",
            “lastname” : "mumbi",
            “email” : "carolmumbi@gmail.com",
            ”phoneNumber” : "0708123123",
            “username” : "carolmobic", 
            “registered” : 26/11/2018,
            “isAdmin” : False,
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
            “id” : 1, 
            “firstname” : "admin",
            “lastname” : "admin",
            “othernames” : "admin",
            “email” : "admin@gmail.com",
            ”phoneNumber” : "0711123123",
            “username” : "admin", 
            “registered” : 26/11/2018,
            “isAdmin” : True,
            ...
            }

        self.admin_correct = {"username": "admin",
                              "password": "admn1234"}
        self.admin_wrong = {"username": "lawrence",
                            "password": "mimi"}

        self.red_flag = {
            "createdOn" : datetime.now,  
            "createdBy" : "carolmobic", 
            "type" : "RedFlag",
            "title": "NCA site auth",
            "location" : "37.12N, 3.7E",
            "status": "pending",
            "Images" : [Image, Image], 
            "Videos" : [Image, Image],
            "comment" : "falling  building"
            }

        self.update_redflag ={
            "createdOn" : datetime.now,  
            "createdBy" : "carolmobic", 
            "type" : "RedFlag",
            "title": "NCA site auth",
            "location" : "37.12N, 3.7E",
            "status": "pending",
            "Images" : [Image, Image], 
            "Videos" : [Image, Image],
            "comment" : "falling construction building"
            }
        self.update_redflag_no_comment ={
            "createdOn" : datetime.now,  
            "createdBy" : "carolmobic", 
            "type" : "RedFlag",
            "title": "NCA site auth",
            "location" : "37.12N, 3.7E",
            "status": "pending",
            "Images" : [Image, Image], 
            "Videos" : [Image, Image],
            "comment" : ""
            }
        self.update_redflag_no_title={
            "createdOn" : datetime.now,  
            "createdBy" : "carolmobic", 
            "type" : "RedFlag",
            "title": "",
            "location" : "37.12N, 3.7E",
            "status": "pending",
            "Images" : [Image, Image], 
            "Videos" : [Image, Image],
            "comment" : "falling construction building"
            }
        self.redflags = [
            {
                "id": 1,
                "createdOn" : datetime.now,  
                "createdBy" : "carolmobic", 
                "type" : "RedFlag",
                "title": "NCA site auth",
                "location" : "37.12N, 3.7E",
                "status": "pending",
                "Images" : [Image, Image], 
                "Videos" : [Image, Image],
                "comment" : "falling construction building"
            },
            {
                "id": 2,
                "createdOn" : datetime.now,  
                "createdBy" : "carolmobic", 
                "type" : "Intervention",
                "title": "corrupt police",
                "location" : "37.12N, 3.7E",
                "status": "resolved",
                "Images" : [Image, Image], 
                "Videos" : [Image, Image],
                "comment" : "traffic police takng bribes"
            },
            {
                "id": 3,
                "createdOn" : datetime.now,  
                "createdBy" : "carolmobic", 
                "type" : "RedFlag",
                "title": "NCA site auth",
                "location" : "37.12N, 3.7E",
                "status": "pending",
                "Images" : [Image, Image], 
                "Videos" : [Image, Image],
                "comment" : "falling construction building"
            },
            {
                "id": 4,
                "createdOn" : datetime.now,  
                "createdBy" : "carolmobic", 
                "type" : "RedFlag",
                "title": "NCA site auth",
                "location" : "37.12N, 3.7E",
                "status": "pending",
                "Images" : [Image, Image], 
                "Videos" : [Image, Image],
                "comment" : "falling construction building"
            }
        ]
        self.redflag_no_title = {
            "createdOn" : datetime.now,  
            "createdBy" : "carolmobic", 
            "type" : "RedFlag",
            "title": "",
            "location" : "37.12N, 3.7E",
            "status": "pending",
            "Images" : [Image, Image], 
            "Videos" : [Image, Image],
            "comment" : "falling construction building"
        }
        self.redflag_no_comment = {
            "createdOn" : datetime.now,  
            "createdBy" : "carolmobic", 
            "type" : "RedFlag",
            "title": "NCA site auth",
            "location" : "37.12N, 3.7E",
            "status": "pending",
            "Images" : [Image, Image], 
            "Videos" : [Image, Image],
            "comment" : ""
        }
        self.redflag_invalid_title = {
            "createdOn" : datetime.now,  
            "createdBy" : "carolmobic", 
            "type" : 12345,
            "title": "NCA site auth",
            "location" : "37.12N, 3.7E",
            "status": "pending",
            "Images" : [Image, Image], 
            "Videos" : [Image, Image],
            "comment" : "falling construction building"
        }
        self.status_Resolved = {
            "status": "Resolved"
        }
        self.status_Rejected = {
            "status": "Rejected"
        }

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
