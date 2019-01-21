from datetime import datetime


from ....database import db_con
from .base_models import BaseModels


class MeetupModel(BaseModels):
    def __init__(self):
        super().__init__('meetups')
        self.connect = db_con()
        
        
    def get_all(self):
        self.cur = self.connect.cursor()
        query = """SELECT * FROM meetups WHERE happening_on >= NOW();"""
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def create_meetup(self, meetup):
        self.cur = self.connect.cursor()
        query = """INSERT INTO meetups (location,images,topic,happening_on,tags)\
        VALUES ('{}','{}','{}','{}','{}') RETURNING json_build_object('meetup_id',meetup_id,'topic',topic,'location',location,'happening_on',happening_on,'tags',tags);""".format(meetup['location'],meetup['images'],meetup['topic'],meetup['happening_on'],meetup['tags'])
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


