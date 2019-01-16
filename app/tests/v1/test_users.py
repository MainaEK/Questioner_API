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

    def test_login_user(self):
        """ Test to login a user."""
        self.users_detail = { "user_id":1,"firstname": "Eric", "lastname": "Maina","othername" : "EM","email": "maina_eric@hotmail.com",
        "phone_number": "1234","username": "maina_eric", "registered_on": "2000-03-03", "password":"Erick1234"}
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.users_detail), content_type = 'application/json')
        self.user_login = {"username": "maina_eric","password":"Erick1234"}
        response = self.client.post('/api/v1/auth/login', data=json.dumps(self.user_login), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        