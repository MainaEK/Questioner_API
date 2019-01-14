import json
import unittest
from ... import create_app


class TestQuestioner(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.questions = {"q_id":"1","created_on" : "01/01/2000", "created_by":"1", "meetup":"1",
                 "title":"Posting in Python", "body":"How?", "votes": "3"}
     
    def test_post_question(self):
        """ Test posting a question."""
        response = self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_downvote_a_question(self):
        """ Test editing a question."""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        response = self.client.patch('/api/v1/question/1/downvote', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 201)    

    def test_upvote_a_question(self):
        """ Test editing a question."""
        self.client.post('/api/v1/questions', data=json.dumps(self.questions), content_type = 'application/json')
        response = self.client.patch('/api/v1/question/1/upvote', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 201)    



if __name__ == '__main__':
    unittest.main()                    
