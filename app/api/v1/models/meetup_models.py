from datetime import datetime
from ..utils.generator import generator

meetups = []

class MeetupModel():
    def __init__(self):
        self.db = meetups

    def get_all(self):
        '''Function to return all meetups'''
        return self.db
    
    def create(self, data):
        '''Function to save new meetup'''
        data['m_id'] = generator(meetups)
        data['created_on'] = datetime.now()
        data['location'] = 'location'
        data['images'] = []
        data['topic'] = 'topic'
        data['happening_on'] = 'happening_on'
        data['tags'] = []
        meetups.append(data)
        return data    

    def get_specific_meetup(self,m_id):
        '''Function using the m_id to check for meetups'''
        fetch_meetup = [meetup for meetup in meetups if meetup[m_id] == m_id]
        return fetch_meetup[0]
