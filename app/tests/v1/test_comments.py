# standard imports
import json
import unittest

#local imports
from ... import create_app


class TestQuestioner(unittest.TestCase):
    
    def setUp(self):
        """ Setting up the test"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.questions = {"q_id":1,"created_on" : "2000-01-01", "created_by":"1", "meetup":"1",
                 "title":"Posting in Python", "body":"How?", "votes": 3}

    def test_post_comment(self):
        """ Test posting a comment."""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        self.comment = {"q_id":1,"comment" : "Good question"}
        response = self.client.post('/api/v1/comments', data=json.dumps(self.comment), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_comment_no_data(self):
        """ Test posting a comment with no data"""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        self.comment = {}
        response = self.client.post('/api/v1/comments', data=json.dumps(self.comment), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_comment_empty_data_fields(self):
        """ Test posting a comment with an empty field which is required"""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        self.comment = {"q_id":1,"comment" : ""}
        response = self.client.post('/api/v1/comments', data=json.dumps(self.comment), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_comment_not_valid_question(self):
        """ Test posting a comment on a question that is not there in the db"""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        self.comment = {"q_id":2,"comment" : "Good question"}
        response = self.client.post('/api/v1/comments', data=json.dumps(self.comment), content_type='application/json')
        self.assertEqual(response.status_code, 404)
