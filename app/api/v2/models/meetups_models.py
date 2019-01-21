from datetime import datetime

from ....database import db_con



class MeetupModel():
    def __init__(self):
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
        VALUES ('{}','{}','{}','{}','{}') RETURNING json_build_object('m_id',m_id,'topic',topic,'location',location,'happening_on',happening_on,'tags',tags);""".format(meetup['location'],meetup['images'],meetup['topic'],meetup['happening_on'],meetup['tags'])
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result

