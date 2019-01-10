from datetime import datetime
from ..utils.generator import generate_id

meetups = []

class Meetup(object):
    """ Model class for the meetup object """

    def __init__(self):
        self.db = meetups

    def save(self, meetup ={"m_id" : "", "created_on" : datetime.date.today(), "location":"", "images":[],
                 "topic":"", "happening_on":"", "tags":[]}):
        """ Function to save new meetup """
        super().__init__(m_id = generate_id)
        self.db.append(meetup)
        return self.db
        

    def fetch_using_id(self, m_id):
        """ Function to fetch meetups by ID """
        fetched_meetups = [meetup for meetup in self.db if meetup['m_id'] == m_id]
        return fetched_meetups[0]

    def all(self):
        """ Function to fetch all meetups """
        return self.db