"""Test for methods applied to Red Flags"""
import json
from app.tests.v2.base import BaseTestCase

class TestIncidentsTestCase(BaseTestCase):
    """Tests for redflags"""

    def signup(self):
        """ 
             create a test user 
        """
        response = self.app.post('/api/v2/auth/signup/',
                                 data=json.dumps(self.person_existing_user),
                                 headers={'content-type': 'application/json'}
                                 )

        return response

    def login(self):
        """
            sign in a user
        """
        response = self.app.post('api/v2/auth/login/',
                                 data=json.dumps(self.correct_login1),
                                 headers={'content-type': 'application/json'})
        return response

    def get_jwt_token(self):
        """
            get jwt token
        """
        self.signup()
        t = self.login()
        data = json.loads(t.get_data())   
        self.data = data.get("data")[0]
        self.token = self.data.get('token')
        return self.token

    def post_incident(self, data):
        """
            post a redflag
        """
        self.get_jwt_token()
        token = self.token
        redflag = self.app.post('/api/v2/incidents/',
                                data=json.dumps(data),
                                headers={'content-type': 'application/json',
                                         'Authorization': token})
        return redflag

    def put_incident(self, data):
        """
            post a redflag
        """
        self.get_jwt_token()
        token = self.token
        redflag = self.app.put('/api/v2/incidents/1/',
                                data=json.dumps(data),
                                headers={'content-type': 'application/json',
                                         'Authorization': token})
        return redflag
    def patch_comment(self, id, data):
        """
            post a redflag
        """
        self.get_jwt_token()
        token = self.token
        redflag = self.app.patch('/api/v2/incidents/'+id+'/comment',
                                data=json.dumps(data),
                                headers={'content-type': 'application/json',
                                         'Authorization': token})
        return redflag

    def patch_location(self, id, data):
        """
            post a redflag
        """
        self.get_jwt_token()
        token = self.token
        redflag = self.app.patch('/api/v2/incidents/'+id+'/location',
                                data=json.dumps(data),
                                headers={'content-type': 'application/json',
                                         'Authorization': token})
        return redflag

    def test_app_works(self):
        response = self.app.get('api/v2')
        self.assertEqual(response.status_code, 301)

    def test_post_incident(self):
        """Test for posting an incident"""
        # correct request
        response = self.post_incident(self.red_flag2)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Created incident successfully!')

    def test_post_incident_exists(self):
        """Test for posting an incident twice"""
        # correct request
        self.post_incident(self.red_flag2)
        response = self.post_incident(self.red_flag2)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Incident already exists')
    
    def test_missing_token(self):
        """Test for posting an incident"""
        # correct request
        response = self.app.post('/api/v2/incidents/',
                                data=json.dumps(self.red_flag3),
                                headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Missing Authorization Header')

    
    def test_post_incident_not_json(self):
        """Test for posting an incident"""
        
        response = self.post_incident(self.red_flag3)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Input payload validation failed')

    def test_new_incident_no_title(self):
        """Test for posting a redflag without title"""
        #no title
        response = self.post_incident(self.redflag_no_title)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'],"Title is invalid or empty")

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
        self.assertEqual(data['error'], 'Images link is invalid')

    def test_new_incident_invalid_video(self):
        """Test for posting a redflag without a valid link video"""
        #no body
        response = self.post_incident(self.redflag_invalid_video)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Video link is invalid')
    
    def test_new_incident_invalid_location(self):
        """Test for posting a redflag without a vali location image"""
        #no body
        response = self.post_incident(self.redflag_invalid_location)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'location input  is invalid')

    def test_new_incident_invalid_type(self):
        """Test for posting a redflag without a valid type"""
        #no body
        response = self.post_incident(self.redflag_invalid_type)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Type is invalid or empty')

    def test_view_all_incidents(self):
        """Test for viewing all incidents"""
        self.post_incident(self.red_flag)
        response = self.app.get('/api/v2/incidents/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "All incidents found successfully")

    def test_view_an_incident(self):
        """Test for vieving a particular redflag"""
        # existing redflag
        self.post_incident(self.red_flag)
        response = self.app.get('/api/v2/incidents/1/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Incident successfully retrieved!")

    def test_view_incident_not_found(self):
        """Test for viewing an incident that does not exist"""
        # redflag does not exist
        response = self.app.get('/api/v2/incidents/1344/')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "Incident not found")

    def test_modify_location(self):
        """Test for modifying an incident location """
        self.post_incident(self.red_flag)
        response = self.patch_location('1',self.redflag_location)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "location successfully updated")

    def test_modify_location_not_found(self):

        self.post_incident(self.red_flag)
        response = self.patch_location('120', self.update_redflag)
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "Incindent not found")

    def test_modify_comment(self):
        """Test for modifying an incident comment """
        self.post_incident(self.red_flag)
        response = self.patch_comment('1',self.redflag_comment)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "comment successfully updated")

    def test_modify_comment_not_found(self):

        self.post_incident(self.red_flag)
        response = self.patch_comment('120', self.update_redflag)
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "Incindent not found")

    def test_delete_an_incident(self):
        """Test for deleting a redflag"""
        self.post_incident(self.red_flag)
        token = self.token
        response = self.app.delete('/api/v2/incidents/1/',
                                   headers={'content-type': 'application/json',
                                            'Authorization': token})
        self.assertEqual(response.status_code, 200)

    def test_delete_incident_not_found(self):

        self.post_incident(self.red_flag)
        token = self.token
        response = self.app.delete('/api/v2/incidents/2222/',
                                   headers={'content-type': 'application/json',
                                            'Authorization': token})
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "Incident not found")

    def test_not_allowed(self):

        self.post_incident(self.red_flag)
        token = self.token
        response = self.app.patch('/api/v2/incidents/2222/',
                                   headers={'content-type': 'application/json',
                                            'Authorization': token})
        self.assertEqual(response.status_code, 405)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], "Method is not allowed on this url")
    def test_update_incident(self):
        """Test for updating an incident"""
        # correct request
        self.post_incident(self.red_flag2)
        response = self.put_incident(self.update_redflag)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Incident updated successfully!')

    def test_update_incident_no_title(self):
        """Test for updating an incident"""
        self.post_incident(self.red_flag2)
        response = self.put_incident( self.redflag_no_title)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Title is invalid or empty')

    def test_update_incident_no_image(self):
        """Test for updating an incident"""
        self.post_incident(self.red_flag2)
        response = self.put_incident( self.redflag_invalid_image)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Images link is invalid')

    def test_update_incident_no_location(self):
        """Test for updating an incident"""
        self.post_incident(self.red_flag2)
        response = self.put_incident( self.redflag_invalid_location )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'location input  is invalid')

    def test_update_incident_no_comment(self):
        """Test for updating an incident"""
        self.post_incident(self.red_flag2)
        response = self.put_incident( self.redflag_no_comment )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'comment is invalid or empty')

    def test_update_incident_not_found(self):
        """Test for updating an incident"""
        self.post_incident(self.red_flag2)
        token = self.token
        response = self.app.put('/api/v2/incidents/123/',
                                data=json.dumps(self.red_flag ),
                                headers={'content-type': 'application/json',
                                         'Authorization': token})
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Incident not found')

    def test_update_incident_not_json(self):
        """Test for updating an incident"""

        self.post_incident(self.red_flag2)        
        response = self.put_incident(self.red_flag3)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Input payload validation failed')