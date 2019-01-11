from datetime import datetime
from ..utils.generator import generator

meetups = []

class MeetupModel():
    def __init__(self):
        self.db = meetups

    def get_all(self):
        '''Function to return all meetups'''
        return self.db
