""" This is the base class for all the tests"""

import unittest
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
