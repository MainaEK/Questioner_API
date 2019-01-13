from flask import Flask, jsonify

meetup_list = []
question_list = []
collection = []


class BaseModels(object):
    def __init__(self, db):
        self.db = db


    def check_db(self):
        if self.db == 'meetup':
            return meetup_list
        elif self.db == 'question':
            return question_list


    def check_exists(self, key, value):
        db = self.check_db()
        items = [item for item in db if item[key] == value]
        return len(items) > 0

    def find(self, key, value):
        db = self.check_db()
        items = [item for item in db if item[key] == value]
        return items[0]

    def return_data(self):
        db = self.check_db()
        return db

    def save(self,data):
        db = self.check_db()
        db.append(data)
        return data 
    