"""
This module contains the tests for the comment endpoints
"""
# standard imports
import json
import unittest

# local imports
from .. import create_app


class TestQuestioner(unittest.TestCase):
    """Class that holds the tests for comments"""

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
        self.questions = {"title": "Posting in Python", "body": "How?"}
        self.meetups = {"location": "Nairobi", "images": ["screenshot"],
                        "topic": "Python", "happening_on": "2019-02-02", "tags": ["python"]}

    def test_post_comment(self):
        """ Test posting a comment."""
        self.client.post('/api/v2/meetups',
                         data=json.dumps(self.meetups), headers=self.headers)
        self.client.post('/api/v2/meetups/1/questions',
                         data=json.dumps(self.questions), headers=self.headers)
        self.comment = {"comment": "Good question"}
        response = self.client.post(
            '/api/v2/questions/1/comments', data=json.dumps(self.comment), headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_post_comment_not_registered(self):
        """ Test posting a comment by a non registered user."""
        self.comment = {"comment": "Good question"}
        response = self.client.post('/api/v2/questions/1/comments',
                                    data=json.dumps(self.comment), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_post_comment_no_data(self):
        """ Test posting a comment with no data"""
        self.comment = {}
        response = self.client.post(
            '/api/v2/questions/1/comments', data=json.dumps(self.comment), headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_post_comment_empty_data_fields(self):
        """ Test posting a comment with an empty field which is required"""
        self.comment = {"comment": ""}
        response = self.client.post(
            '/api/v2/questions/1/comments', data=json.dumps(self.comment), headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_post_comment_invalid_question(self):
        """ Test posting a comment."""
        self.comment = {"comment": "Good question"}
        response = self.client.post(
            '/api/v2/questions/100/comments', data=json.dumps(self.comment), headers=self.headers)
        self.assertEqual(response.status_code, 404)
