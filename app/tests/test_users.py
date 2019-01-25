"""
This module contains the tests for the user endpoints
"""
# standard imports
import json
import unittest

# local imports
from .. import create_app


class TestQuestioner(unittest.TestCase):
    """Class that holds the tests for questions"""

    def setUp(self):
        """Setting up the tests"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.users = {"firstname": "Eric", "lastname": "Maina", "othername": "EM", "email": "maina@hotmail.com",
                      "phone_number": "1234", "username": "maina", "password": "Erick1234"}

    def test_signup_user(self):
        """ Test signing up a new user."""
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.users), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_signup_user_no_data(self):
        """ Test signing up a new user with no data"""
        self.user = {}
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_signup_user_same_username(self):
        """ Test signing up two users with the same username"""
        self.user = {"firstname": "Eric", "lastname": "Maina", "othername": "EM", "email": "maina_eric@hotmail.com",
                     "phone_number": "1234", "username": "eric", "password": "Erick1234"}
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_signup_user_same_email(self):
        """ Test signing up two users with the same email"""
        self.user = {"user_id": 1, "firstname": "Eric", "lastname": "Maina", "othername": "EM", "email": "admin@hotmail.com",
                     "phone_number": "1234", "username": "maina_eric", "password": "Erick1234"}
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_signup_user_empty_fields(self):
        """ Test signing up a new user with empty required fields."""
        self.user = {"firstname": "Eric", "lastname": "Maina", "othername": "EM", "email": "c_maina@hotmail.com",
                     "phone_number": "1234", "username": "", "password": "Erick1234"}
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.users), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_user(self):
        """ Test to login a user."""
        self.user_login = {"username": "eric", "password": "Eric1234"}
        response = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.user_login), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_user_no_data(self):
        """ Test to login a user using no data"""
        self.user_login = {}
        response = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.user_login), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_user_invalid_user(self):
        """ Test to login a user who isn't registered"""
        self.user_login = {"username": "ericmaina", "password": "Erick1234"}
        response = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.user_login), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_login_user_invalid_password(self):
        """ Test to login a user using a wrong password"""
        self.user_login = {"username": "eric", "password": "Erick13"}
        response = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.user_login), content_type='application/json')
        self.assertEqual(response.status_code, 400)
