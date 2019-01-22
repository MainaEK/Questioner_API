
from .base_models import BaseModels


class MeetupModel(BaseModels):
    def __init__(self):
        super().__init__('meetups')
        
        
    def get_all(self):
        self.cur = self.connect.cursor()
        query = """SELECT json_build_object('meetup_id',meetup_id,'topic',topic,'location',location,'happening_on',happening_on,
        'created_on',created_on,'modified_on',modified_on,'images',images,'tags',tags) 
                FROM (SELECT * FROM meetups WHERE happening_on >= NOW()) AS get_all;"""
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def create_meetup(self, meetup):
        self.cur = self.connect.cursor()
        images = "{" 
        for image in meetup['images']:
            images += '"' + image + '",'
        images = images[:-1] + "}"                                                                                                       
        tags = "{" 
        for tag in meetup['tags']:
            tags += '"' + tag + '",'
        tags = tags[:-1] + "}"

        query = """INSERT INTO meetups (location,images,topic,happening_on,tags)\
        VALUES ('{}','{}','{}','{}','{}') RETURNING json_build_object('meetup_id',meetup_id,'topic',topic,'location',location,'happening_on',happening_on,'tags',tags)
        ;""".format(meetup['location'],images,meetup['topic'],meetup['happening_on'],tags)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result

    def find(self, m_id):
        self.cur = self.connect.cursor()
        query = """SELECT json_build_object('meetup_id',meetup_id,'topic',topic,'location',location,'happening_on',happening_on,'tags',tags) 
                FROM ( SELECT meetup_id,topic,location,happening_on,tags FROM meetups WHERE meetup_id = {}) AS found;""".format(m_id)
        self.cur.execute(query)
        result = self.cur.fetchone()
        print(result)
        return result

    def delete(self, m_id):
        """ Function to delete meetup """
        self.cur = self.connect.cursor()
        query = """DELETE FROM meetups WHERE meetup_id = {};""".format(m_id)
        self.cur.execute(query)
        self.connect.commit()


