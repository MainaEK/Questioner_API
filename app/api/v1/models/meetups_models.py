from datetime import datetime
from ..utils.generator import generate_id
from .base_models import BaseModels


class MeetupModel(BaseModels):
    def __init__(self):
        super().__init__('meetup')
        
    def get_all(self):
        response = self.db.return_data()
        return response


    def save(self, meetup):
        meetup = {
            'm_id' : generate_id(self.return_data),
            'created_on' : datetime.now(),
            'location' : meetup['location'],
            'images' : meetup['images'],
            'topic' : meetup['topic'],
            'happening_on' : meetup['happening_on'],
            'tags': meetup['tags']
        }
        response = self.save(meetup)
        return response
        