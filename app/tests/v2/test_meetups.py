#standard imports
import json
import unittest

# local imports
from ... import create_app
from ...database import db_con_test,destroy
from ...db_tables import create_db

class TestQuestioner(unittest.TestCase):
    """ Setting up the test"""
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        try:
            connect = db_con_test()
            create_db(connect)    
        except Exception:
            print("Unable to make db connection")
        self.meetups = {"location": "Nairobi","images": "screenshot",
        "topic": "Python","happening_on": "2000-02-02", "tags": "python"}

    def test_view_all_upcoming_meetups(self):
        """ Test view all meetups."""
        self.client.post('/api/v2/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.get('/api/v2/meetups/upcoming', content_type='application/json')
        self.assertEqual(response.status_code, 200) 

    def test_post_meetup(self):
        """ Test posting a meetup."""
        response = self.client.post('/api/v2/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_meetup_no_data(self):
        """ Test posting a meetup with no data input"""
        self.meetup = { }
        response = self.client.post('/api/v2/meetups', data=json.dumps(self.meetup), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_meetup_empty_data_fields(self):
        """ Test posting a meetup with empty data fields"""
        self.meetup = { "location": "","images": "screenshot",
        "topic": "Python","happening_on": "2000-02-02", "tags": "python"}
        response = self.client.post('/api/v2/meetups', data=json.dumps(self.meetup), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        destroy()
        