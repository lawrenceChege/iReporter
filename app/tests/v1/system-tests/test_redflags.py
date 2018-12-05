"""Test for methods applied to Red Flags"""
import json
from app.tests.v1.base import BaseTestCase


class TestIncidentsTestCase(BaseTestCase):
    """Tests for redflags"""

    def signup(self):
        """ 
             create a test user 
        """
        response = self.app.post('/api/v1/auth/signup/',
                                 data=json.dumps(self.person),
                                 headers={'content-type': 'application/json'}
                                 )

        return response

    def login(self):
        """
            sign in a user
        """
        response = self.app.post('api/v1/auth/login/',
                                 data=json.dumps(self.correct_login),
                                 headers={'content-type': 'application/json'})
        return response

    def get_jwt_token(self):
        """
            get jwt token
        """
        self.signup()
        t = self.login()
        data = json.loads(t.get_data())
        self.token = data["data"][0]["token"]
        return self.token

    def post_incident(self, data):
        """
            post a redflag
        """
        self.get_jwt_token()
        token = self.token
        redflag = self.app.post('/api/v1/incidents/',
                                data=json.dumps(data),
                                headers={'content-type': 'application/json',
                                         'Authorization': token})
        return redflag

    def test_app_works(self):
        response = self.app.get('api/v1')
        self.assertEqual(response.status_code, 301)

    def test_post_incident(self):
        """Test for posting an incident"""
        # correct request
        response = self.post_incident(self.red_flag2)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Redflag posted successfully!')

    def test_new_incident_no_title(self):
        """Test for posting a redflag without title"""
        #no title
        response = self.post_incident(self.redflag_no_title)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],"Input payload validation failed")

    def test_new_incident_no_comment(self):
        """Test for posting a redflag without a body"""
        #no description
        response = self.post_incident(self.redflag_no_comment)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'description is invalid or empty')
    
    def test_new_incident_invalid_image(self):
        """Test for posting a redflag without a vali link image"""
        #no body
        response = self.post_incident(self.redflag_invalid_image)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Input payload validation failed')

    def test_view_all_incidents(self):
        """Test for viewing all incidents"""
        self.post_incident(self.red_flag)
        response = self.app.get('/api/v1/incidents/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "All redflags found successfully")

    def test_view_an_incident(self):
        """Test for vieving a particular redflag"""
        # existing redflag
        self.post_incident(self.red_flag)
        response = self.app.get('/api/v1/incidents/1/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Redflag successfully retrieved!")

    def test_view_incident_not_found(self):
        """Test for viewing an incident that does not exist"""
        # redflag does not exist
        response = self.app.get('/api/v1/incidents/1344/')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "Redflag not found")

    def test_modify_an_incident(self):
        """Test for modifying an incident """
        self.post_incident(self.redflag_invalid_video)
        token = self.token
        response = self.app.put('/api/v1/incidents/1/',
                                data=json.dumps(self.update_redflag),
                                headers={'content-type': "application/json",
                                         'Authorization': token})
        self.assertEqual(response.status_code, 200)

    def test_modify_incident_not_found(self):

        self.post_incident(self.red_flag)
        token = self.token
        response = self.app.put('/api/v1/incidents/143/',
                                data=json.dumps(self.update_redflag),
                                headers={'content-type': "application/json",
                                         'Authorization': token})
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "Redflag not found")

    def test_delete_an_incident(self):
        """Test for deleting a redflag"""
        self.post_incident(self.red_flag)
        token = self.token
        response = self.app.delete('/api/v1/incidents/1/',
                                   headers={'content-type': 'application/json',
                                            'Authorization': token})
        self.assertEqual(response.status_code, 404)

    def test_delete_incident_not_found(self):

        self.post_incident(self.red_flag)
        token = self.token
        response = self.app.delete('/api/v1/incidents/2222/',
                                   headers={'content-type': 'application/json',
                                            'Authorization': token})
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "Redflag not found")
