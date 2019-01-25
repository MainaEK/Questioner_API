"""
This module contains the tests for the meetups endpoints
"""
# standard imports
import json
import unittest


# local imports
from .. import create_app


class TestQuestioner(unittest.TestCase):
    """Class that holds the tests for questions"""

    def setUp(self):
        """ Setting up the test"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.user = {"username": "eric", "password": "Eric1234"}
        auth = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.user), content_type='application/json')
        token = auth.json['data'][0]['token']
        self.headers = {"Content-Type": "application/json"}
        self.headers['Authorization'] = 'Bearer {}'.format(token)

    def test_view_all_upcoming_meetups(self):
        """ Test view all upcoming meetups."""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-02-02", "tags": ["python"]}
        self.client.post('/api/v2/meetups',
                         data=json.dumps(self.meetups), headers=self.headers)
        response = self.client.get(
            '/api/v2/meetups/upcoming', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_post_meetup(self):
        """ Test posting a meetup."""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-02-03", "tags": ["python"]}
        response = self.client.post(
            '/api/v2/meetups', data=json.dumps(self.meetups), headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_post_similar_meetups(self):
        """ Test posting similar meetups."""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-03-04", "tags": ["python"]}
        self.meetup = {"location": "Nairobi", "images": ["screenshot"],
                       "topic": "Python", "happening_on": "2019-03-04", "tags": ["python"]}
        self.client.post('/api/v2/meetups',
                         data=json.dumps(self.meetups), headers=self.headers)
        response = self.client.post(
            '/api/v2/meetups', data=json.dumps(self.meetup), headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_post_meetup_not_admin(self):
        """ Test posting a meetup by a non admin."""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-02-04", "tags": ["python"]}
        response = self.client.post(
            '/api/v2/meetups', data=json.dumps(self.meetups), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_post_meetup_no_data(self):
        """ Test posting a meetup with no data input"""
        self.meetup = {}
        response = self.client.post(
            '/api/v2/meetups', data=json.dumps(self.meetup), headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_post_meetup_empty_data_fields(self):
        """ Test posting a meetup with empty data fields"""
        self.meetup = {"location": "", "images": ["screenshot"],
                       "topic": "Python", "happening_on": "2020-02-02", "tags": ["python"]}
        response = self.client.post(
            '/api/v2/meetups', data=json.dumps(self.meetup), headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_specific_meetup(self):
        """ Test view a single specific meetup."""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-02-06", "tags": ["python"]}
        self.client.post('/api/v2/meetups',
                         data=json.dumps(self.meetups), headers=self.headers)
        response = self.client.get(
            '/api/v2/meetups/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_meetup_not_valid_meetup(self):
        """ Test to view a meetup that doesn't exist"""
        response = self.client.get(
            '/api/v2/meetups/200', content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_post_rsvp(self):
        """ Test posting a rsvp."""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-02-07", "tags": ["python"]}
        response = self.client.post(
            '/api/v2/meetups/1/yes', data=json.dumps(self.meetups), headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_post_rsvp_not_registered_user(self):
        """ Test posting a rsvp by a non registered user."""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-02-08", "tags": ["python"]}
        response = self.client.post(
            '/api/v2/meetups/1/yes', data=json.dumps(self.meetups), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_post_rsvp_not_valid_meetup(self):
        """ Test posting a rsvp to a meetup that doesn't exist"""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-02-09", "tags": ["python"]}
        response = self.client.post(
            '/api/v2/meetups/200/yes', data=json.dumps(self.meetups), headers=self.headers)
        self.assertEqual(response.status_code, 404)

    def test_post_rsvp_not_valid_rsvp(self):
        """ Test posting a rsvp with an invalid rsvp"""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-02-10", "tags": ["python"]}
        response = self.client.post(
            '/api/v2/meetups/1/y', data=json.dumps(self.meetups), headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_delete_meetup(self):
        """ Test deleting a meetup."""
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-03-03", "tags": ["python"]}
        self.meetup = {"location": "Nairobi", "images": ["screenshot"],
                       "topic": "Python", "happening_on": "2019-03-02", "tags": ["python"]}
        self.client.post('/api/v2/meetups',
                         data=json.dumps(self.meetups), headers=self.headers)
        self.client.post('/api/v2/meetups',
                         data=json.dumps(self.meetup), headers=self.headers)
        response = self.client.delete(
            '/api/v2/meetups/2', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_meetup_not_admin(self):
        """ Test deleting a meetup by a non admin."""
        response = self.client.delete(
            '/api/v2/meetups/1', content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_delete_meetup_not_valid_meetup(self):
        """ Test deleting a meetup that does't exist"""
        response = self.client.delete(
            '/api/v2/meetups/200', headers=self.headers)
        self.assertEqual(response.status_code, 404)
