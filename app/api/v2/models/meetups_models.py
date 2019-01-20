from datetime import datetime

from .base_models import BaseModels
from ....database import db_con

connect = db_con()

class MeetupModel(BaseModels):
    def __init__(self):
        super().__init__('meetups')
        
        
        
    def get_all(self):
        self.cur = connect.cursor()
        query = """SELECT * FROM meetups WHERE happening_on >= NOW();"""
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result



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
        
        