"""Test for methods applied to Red Flags"""
import json
from api.tests.base import BaseTestCase


class TestRequestsTestCase(BaseTestCase):
    """Tests for Questions"""

    def test_new_redflag(self):
        """Test for posting a redflag"""
        #correct request
        response = self.app.post('/api/v1/redflags/', data=json.dumps(
            self.redflag), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Redflag posted successfully!')

    def test_new_redflag_no_title(self):
        """Test for posting a redflag without title"""
        #no title
        response = self.app.post('/ireporter/api/v1/red-flags/', data=json.dumps(
            self.redflag_no_title), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Title is required')

    def test_new_redflag_no_comment(self):
        """Test for posting a redflag without a body"""
        #no body
        response = self.app.post('/ireporter/api/v1/red-flags/', data=json.dumps(
            self.redflag_no_comment), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Body is required')

    def test_view_all_redflags(self):
        """Test for viewing all redflags"""
        response = self.app.get('/ireporter/api/v1/red-flags/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], "All redflags found successfully")

    def test_view_a_redflag(self):
        """Test for vieving a particular redflag"""
        #existing redflag
        response = self.app.get('/ireporter/api/v1/red-flags/redflag/1/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], "Redflag successfully retrieved")

    def test_view_reflag_not_found(self):
        """Test for viewing a redflag that does not exist"""
        #redflag does not exist
        response = self.app.get('/ireporter/api/v1/red-flags/redflag/1344/')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Redflag does not exitst!")


    def test_modify_a_redflag(self):
        """Test for modifying a redflag """
        response = self.app.put('/ireporter/api/v1/red-flags/redflag/2/',
                                data=json.dumps(self.update_redflag),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 204)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Redflag updated successfully!")

    def test_user_delete_a_question(self):
        """Test for deleting a redflag"""
        response = self.app.delete('/ireporter/api/v1/red-flags/redflag/2/')
        self.assertEqual(response.status_code, 204)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Redflag successfuly deleted")

