from flask import Flask, jsonify




class BaseModels(object):
    def __init__(self, tablename):
        self.table = tablename


    def check_exists(self, key, value):
        db = self.check_db()
        items = [item for item in db if item[key] == value]
        return len(items) 

    def find(self, key, value):
        db = self.check_db()
        items = [item for item in db if item[key] == value]
        return items[0]


    def save(self,data):
        db = self.check_db()
        db.append(data)
        return data 
    
    def delete(self, key, value):
        """ Function to delete item """
        item = self.find(key, value)
        db = self.check_db()
        db.remove(item)

        