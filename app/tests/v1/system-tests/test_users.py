""" Test for user methods and views"""
import json
from app.tests.base import BaseTestCase

class TestUsersTestCase(BaseTestCase):
    """
         test for users
    """
    def signup(self, user):
        """
             create a test user
        """
        response = self.app.post('/api/v1/auth/signup/',
                                 data=json.dumps(user),
                                 headers={'content-type': 'application/json'}
                                 )

        return response

    def login(self, user):
        """
            sign in a user
        """
        response = self.app.post('api/v1/auth/login/',
                                 data=json.dumps(user),
                                 headers={'content-type': 'application/json'})
        return response


    def test_correct_signup(self):
        """
            test for signup with all required fields
        """
        response = self.signup(self.person1)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        print(data)
        self.assertEqual(data['message'], 'User created Succesfully.')

    def test_signup_existing_user(self):
        """
            test for signup for an existing user
        """
        self.signup(self.person)
        response = self.signup(self.person)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        print(data)
        self.assertEqual(data['error'], 'Username already in use.')

    def test_signup_no_email(self):
        """
            test for signup without an email field
        """
        response = self.signup(self.person_no_email)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Input payload validation failed')

    def test_signup_no_username(self):
        """
            test for signup without an username field
        """
        response = self.signup(self.person_no_username)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Input payload validation failed')

    def test_signup_no_password(self):
        """
            test for signup without a password field
        """
        response = self.signup(self.person_no_password)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Input payload validation failed')

    def test_signup_invalid_username(self):
        """
            test for signup with an invalid username
        """
        response = self.signup(self.person_invalid_username)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Username is invalid or empty')

    def test_signup_invalid_email(self):
        """
            test for signup with an invalid email
        """
        response = self.signup(self.person_invalid_email)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Email is invalid or empty!')

    def test_signup_invalid_password(self):
        """
            test for signup with an invalid username
        """
        response = self.signup(self.person_invalid_password)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Passord is should contain atleast 8 characters, a letter, a number and a special character')

    def test_correct_login(self):
        """
            Test for login with correct user details
        """
        self.signup(self.person)
        response = self.login(self.correct_login)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],'successful' )

    def test_not_found_login(self):
        """
            Test for login with correct user details
        """
        self.signup(self.person)
        response = self.login(self.wrong_login)
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'],'user not found' )

    def test_login_no_username(self):
        """
            Test for login without a username
        """
        self.signup(self.person)
        response = self.login(self.person_no_username)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],'Input payload validation failed' )

    def test_login_no_password(self):
        """
            Test for login without password
        """
        self.signup(self.person)
        response = self.login(self.person_no_password)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],'Input payload validation failed' )

    def test_login_invalid_password(self):
        """
            Test for login with invalid password
        """
        self.signup(self.person)
        response = self.login(self.person_invalid_password)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'],'Passord is should contain atleast 8 characters, a letter, a number and a special character' )

    def test_login_invalid_username(self):
        """
            Test for login with invalid username
        """
        self.signup(self.person)
        response = self.login(self.person_invalid_username)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'],'Username is invalid or empty' )

