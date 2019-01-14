from datetime import datetime
from ..utils.generator import generate_id
from .base_models import BaseModels


class MeetupModel(BaseModels):
    def __init__(self):
        super().__init__('meetup')
        
        
    def get_all(self):
        self.db = BaseModels(db = 'meetup')
        response = self.db.return_data()
        return response



    def create_meetup(self, meetup):
        meetup = {
            'm_id' : meetup['m_id'],
            'created_on' : meetup['created_on'],
            'location' : meetup['location'],
            'images' : meetup['images'],
            'topic' : meetup['topic'],
            'happening_on' : meetup['happening_on'],
            'tags': meetup['tags']
        }
        response = self.save(meetup)
        return response
        