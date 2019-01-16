#standard imports
import json
import unittest

# local imports
from ... import create_app


class TestQuestioner(unittest.TestCase):
    """ Setting up the test"""
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

    def test_post_meetup_no_data(self):
        """ Test posting a meetup with no data input"""
        self.meetup = { }
        response = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_meetup_empty_data_fields(self):
        """ Test posting a meetup with empty data fields"""
        self.meetup = { "m_id":1,"created_on": "2000-01-01", "location": "","images": "screenshot",
        "topic": "Python","happening_on": "2000-02-02", "tags": "python"}
        response = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_specific_meetup(self):
        """ Test view a single meetup."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.get('/api/v1/meetups/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_meetup_not_valid_meetup(self):
        """ Test to view a meetup that doesn't exist"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.get('/api/v1/meetups/2', content_type='application/json')
        self.assertEqual(response.status_code, 404)  
    
    def test_post_rsvp(self):
        """ Test posting a rsvp."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.post('/api/v1/meetups/1/yes', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_rsvp_not_valid_meetup(self):
        """ Test posting a rsvp to a meetup that doesn't exist"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.post('/api/v1/meetups/2/yes', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)

    def test_post_rsvp_not_valid_rsvp(self):
        """ Test posting a rsvp with an invalid rsvp"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.post('/api/v1/meetups/1/y', data=json.dumps(self.meetups), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_delete_meetup(self):
        """ Test deleting a meetup."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.delete('/api/v1/meetups/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_meetup_not_valid_meetup(self):
        """ Test deleting a meetup that does't exist"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        response = self.client.delete('/api/v1/meetups/2', content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_post_tags(self):
        """ Test posting a tag."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.tags ={ "tags": ["python","coding"]}
        response = self.client.post('/api/v1/meetups/1/tags', data=json.dumps(self.tags), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_tags_no_data(self):
        """ Test posting a tag with no data"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.tags ={}
        response = self.client.post('/api/v1/meetups/1/tags', data=json.dumps(self.tags), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_tags_empty_fields(self):
        """ Test posting a tag with empty fields"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.tags ={ "tags": "" }
        response = self.client.post('/api/v1/meetups/1/tags', data=json.dumps(self.tags), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_tags_not_valid_meetup(self):
        """ Test posting a tag to a meetup that doesn't exist"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.tags ={ "tags": ["python","coding"]}
        response = self.client.post('/api/v1/meetups/2/tags', data=json.dumps(self.tags), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)

    def test_post_images(self):
        """ Test posting a tag."""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.images ={ "images": ["python","coding"]}
        response = self.client.post('/api/v1/meetups/1/images', data=json.dumps(self.images), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_images_no_data(self):
        """ Test posting a tag with no data"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.images ={}
        response = self.client.post('/api/v1/meetups/1/images', data=json.dumps(self.images), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_images_empty_fields(self):
        """ Test posting a tag with empty fields"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.images ={ "images": ""}
        response = self.client.post('/api/v1/meetups/1/images', data=json.dumps(self.images), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_images_not_valid_meetup(self):
        """ Test posting a tag to a meetup that doesn't exist"""
        self.client.post('/api/v1/meetups', data=json.dumps(self.meetups), content_type = 'application/json')
        self.images ={ "images": ["python","coding"]}
        response = self.client.post('/api/v1/meetups/2/images', data=json.dumps(self.images), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()  
         