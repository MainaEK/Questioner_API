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
