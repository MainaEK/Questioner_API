# standard imports
import json
import unittest

# local imports
from ... import create_app


class TestQuestioner(unittest.TestCase):
    """ Setting up the test"""
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.questions = {"q_id":1,"created_on" : "2000-01-01", "created_by":"1", "meetup":"1",
                 "title":"Posting in Python", "body":"How?", "votes": 3}
     
    def test_post_question(self):
        """ Test posting a question."""
        response = self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_question_no_data(self):
        """ Test posting a question with no data"""
        self.question = {}
        response = self.client.post('/api/v1/questions', data=json.dumps(self.question), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_question_empty_fields(self):
        """ Test posting a question with empty required fields"""
        self.questions = {"q_id":1,"created_on" : "2000-01-01", "created_by":"1", "meetup":"1",
                 "title":"Posting in Python", "body":"", "votes": 3}
        response = self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_downvote_a_question(self):
        """ Test downvoting a question."""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        response = self.client.patch('/api/v1/questions/1/downvote', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_downvote_to_invalid_question(self):
        """ Test downvoting to an invalid question."""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        response = self.client.patch('/api/v1/questions/2/downvote', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 404)    

    def test_upvote_a_question(self):
        """ Test upvoting a question."""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        response = self.client.patch('/api/v1/questions/1/upvote', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_upvote_to_invalid_question(self):
        """ Test upvoting to an invalid question."""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        response = self.client.patch('/api/v1/questions/2/upvote', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 404)    



if __name__ == '__main__':
    unittest.main()                    
