from flask import Flask, jsonify
from ....database import db_con



class BaseModels(object):
    def __init__(self, tablename):
        self.table = tablename
        self.connect = db_con()

    
    def check_exists(self, key, value):
        self.cur = self.connect.cursor()
        query = """SELECT * FROM {} WHERE {} = {};""".format(self.table, key, value)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return  len(result) > 0

    

    