#standard imports
import json
import unittest
import os 

# local imports
from .. import create_app
from ..database import db_con

class TestQuestioner(unittest.TestCase):
    """ Setting up the test"""
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.user = { "username": "eric", "password":"Eric1234"}
        auth = self.client.post('/api/v2/auth/login', data=json.dumps(self.user), content_type = 'application/json')
        token = auth.json['data'][0]['token']
        self.headers = {"Content-Type": "application/json"}
        self.headers['Authorization'] = 'Bearer {}'.format(token)
        self.meetups = {"location": "Nairobi","images": ["screenshot"],
        "topic": "Python","happening_on": "2019-02-02", "tags": ["python"]}

    def test_view_all_upcoming_meetups(self):
        """ Test view all meetups."""
        self.client.post('/api/v2/meetups', data=json.dumps(self.meetups), headers = self.headers)
        response = self.client.get('/api/v2/meetups/upcoming', headers = self.headers)
        self.assertEqual(response.status_code, 200) 

    def test_post_meetup(self):
        """ Test posting a meetup."""
        response = self.client.post('/api/v2/meetups', data=json.dumps(self.meetups), headers = self.headers)
        self.assertEqual(response.status_code, 201)

    def test_post_meetup_not_admin(self):
        """ Test posting a meetup."""
        response = self.client.post('/api/v2/meetups', data=json.dumps(self.meetups), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_post_meetup_no_data(self):
        """ Test posting a meetup with no data input"""
        self.meetup = { }
        response = self.client.post('/api/v2/meetups', data=json.dumps(self.meetup), headers = self.headers)
        self.assertEqual(response.status_code, 400)

    def test_post_meetup_empty_data_fields(self):
        """ Test posting a meetup with empty data fields"""
        self.meetup = { "location": "","images": ["screenshot"],
        "topic": "Python","happening_on": "2020-02-02", "tags": ["python"]}
        response = self.client.post('/api/v2/meetups', data=json.dumps(self.meetup), headers = self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_specific_meetup(self):
        """ Test view a single meetup."""
        self.client.post('/api/v2/meetups', data=json.dumps(self.meetups), headers = self.headers)
        response = self.client.get('/api/v2/meetups/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_meetup_not_valid_meetup(self):
        """ Test to view a meetup that doesn't exist"""
        response = self.client.get('/api/v2/meetups/200', content_type='application/json')
        self.assertEqual(response.status_code, 404)  
    
    def test_post_rsvp(self):
        """ Test posting a rsvp."""
        response = self.client.post('/api/v2/meetups/1/yes', data=json.dumps(self.meetups), headers = self.headers)
        self.assertEqual(response.status_code, 201)

    def test_post_rsvp_not_registered_user(self):
        """ Test posting a rsvp."""
        response = self.client.post('/api/v2/meetups/1/yes', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)

    def test_post_rsvp_not_valid_meetup(self):
        """ Test posting a rsvp to a meetup that doesn't exist"""
        response = self.client.post('/api/v2/meetups/200/yes', data=json.dumps(self.meetups), headers = self.headers)
        self.assertEqual(response.status_code, 404)

    def test_post_rsvp_not_valid_rsvp(self):
        """ Test posting a rsvp with an invalid rsvp"""
        response = self.client.post('/api/v2/meetups/1/y', data=json.dumps(self.meetups), headers = self.headers)
        self.assertEqual(response.status_code, 400)
    
    def test_delete_meetup(self):
        """ Test deleting a meetup."""
        self.client.post('/api/v2/meetups', data=json.dumps(self.meetups), headers = self.headers)
        self.client.post('/api/v2/meetups', data=json.dumps(self.meetups), headers = self.headers)
        self.client.post('/api/v2/meetups', data=json.dumps(self.meetups), headers = self.headers)
        response = self.client.delete('/api/v2/meetups/2', headers = self.headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_meetup_not_admin(self):
        """ Test deleting a meetup."""
        response = self.client.delete('/api/v2/meetups/1', content_type = 'application/json')
        self.assertEqual(response.status_code, 401)

    def test_delete_meetup_not_valid_meetup(self):
        """ Test deleting a meetup that does't exist"""
        response = self.client.delete('/api/v2/meetups/200', headers = self.headers)
        self.assertEqual(response.status_code, 404)

   