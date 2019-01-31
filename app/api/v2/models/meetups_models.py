"""
This module defines the meetup model and associated functions
"""
from .base_models import BaseModels


class MeetupModel(BaseModels):
    """
    This class encapsulates the functions of the meetup model
    """

    def __init__(self):
        """Initialize the database"""
        super().__init__('meetups')

    def get_all(self):
        """
        Function that returns the upcoming meetups relative to now and 
        in ascending order
        """
        query = """SELECT meetup_id,topic,location,happening_on,tags FROM meetups WHERE happening_on >= NOW();"""
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def create_meetup(self, meetup):
        """Function that creates a meetup in the meetups table"""
        images = "{"
        for image in meetup['images']:
            images += '"' + image + '",'
        images = images[:-1] + "}"

        tags = "{"
        for tag in meetup['tags']:
            tags += '"' + tag + '",'
        tags = tags[:-1] + "}"

        query = """INSERT INTO meetups (location,images,topic,happening_on,tags)\
        VALUES ('{}','{}','{}','{}','{}') RETURNING meetup_id,topic,location,happening_on,tags
        ;""".format(meetup['location'], images, meetup['topic'], meetup['happening_on'], tags)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result

    def find(self, m_id):
        """
        Function that finds and returns information under a particular meetup_id
        """
        query = """SELECT meetup_id,topic,location,happening_on,tags FROM meetups WHERE meetup_id = {}
        ;""".format(m_id)
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result

    def delete(self, m_id):
        """ Function to delete meetup given the meetup_id """
        query = """DELETE FROM meetups WHERE meetup_id = {};""".format(m_id)
        self.cur.execute(query)
        self.connect.commit()

    def check_similar(self, topic, location, happening_on):
        """Function to check for similar meetups 
        already in the database
        """
        query = """SELECT * FROM meetups WHERE topic = '{}' AND location = '{}' AND happening_on = '{}'
        ;""".format(topic, location, happening_on)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return len(result) > 0
