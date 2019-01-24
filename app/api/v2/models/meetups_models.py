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
        self.cur = self.connect.cursor()
        query = """SELECT json_build_object('meetup_id',meetup_id,'topic',topic,'location',location,'happening_on',happening_on,
        'created_on',created_on,'modified_on',modified_on,'images',images,'tags',tags) 
                FROM (SELECT * FROM meetups WHERE happening_on >= NOW()) AS get_all;"""
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

        self.cur = self.connect.cursor()
        query = """INSERT INTO meetups (location,images,topic,happening_on,tags)\
        VALUES ('{}','{}','{}','{}','{}') RETURNING json_build_object('meetup_id',meetup_id,'topic',topic,'location',location,'happening_on',happening_on,'tags',tags)
        ;""".format(meetup['location'], images, meetup['topic'], meetup['happening_on'], tags)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result

    def find(self, m_id):
        """
        Function that finds and returns information under a particular meetup_id
        """
        self.cur = self.connect.cursor()
        query = """SELECT json_build_object('meetup_id',meetup_id,'topic',topic,'location',location,'happening_on',happening_on,'tags',tags) 
                FROM ( SELECT meetup_id,topic,location,happening_on,tags FROM meetups WHERE meetup_id = {}) AS found;""".format(m_id)
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result

    def delete(self, m_id):
        """ Function to delete meetup given the meetup_id """
        self.cur = self.connect.cursor()
        query = """DELETE FROM meetups WHERE meetup_id = {};""".format(m_id)
        self.cur.execute(query)
        self.connect.commit()

    def check_similar(self, topic, location, happening_on):
        """Function to check for similar meetups 
        already in the database
        """
        self.cur = self.connect.cursor()
        query = """SELECT * FROM meetups WHERE topic = '{}' AND location = '{}' AND happening_on = '{}';""".format(
            topic, location, happening_on)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return len(result) > 0
