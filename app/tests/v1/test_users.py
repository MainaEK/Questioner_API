import json
import unittest
from ... import create_app


class TestQuestioner(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.users = { "user_id":1,"firstname": "Eric", "lastname": "Maina","othername" : "EM","email": "eric_maina@hotmail.com",
        "phone_number": "1234","username": "eric_maina", "registered_on": "2000-03-03", "password":"Erick1234"}

    def test_signup_user(self):
        """ Test signing up a new user."""
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.users), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)