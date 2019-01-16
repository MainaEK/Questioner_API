import json
import unittest
from ... import create_app


class TestQuestioner(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.meetups = { "m_id":1,"created_on": "2000-01-01", "location": "Nairobi","images": "screenshot",
        "topic": "Python","happening_on": "2000-02-02", "tags": "python"}
        

    def test_view_all_upcoming_meetups(self):
        """ Test view all meetups."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.get('/api/v1/meetups/upcoming', content_type='application/json')
        self.assertEqual(response.status_code, 200) 

    def test_post_meetup(self):
        """ Test posting a meetup."""
        response = self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_specific_meetup(self):
        """ Test view a single meetup."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.get('/api/v1/meetups/1', content_type='application/json')
        self.assertEqual(response.status_code, 200) 

    
    def test_post_rsvp(self):
        """ Test posting a rsvp."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.post('/api/v1/meetups/1/yes', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_delete_meetup(self):
        """ Test deleting a meetup."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.delete('/api/v1/meetups/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_tags(self):
        """ Test posting a tag."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.tags ={ "tags": ["python","coding"]}
        response = self.client.post('/api/v1/meetups/1/tags', data=json.dumps(self.tags), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_images(self):
        """ Test posting a tag."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.images ={ "images": ["python","coding"]}
        response = self.client.post('/api/v1/meetups/1/images', data=json.dumps(self.images), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()  
         