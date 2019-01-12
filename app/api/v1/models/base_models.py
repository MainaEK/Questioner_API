from flask import Flask, jsonify

meetup_list = []
question_list = []


class BaseModels(object):
    def __init__(self, db):
        self.db = db


    def check_db(self):
        if self.db == 'meetup':
            self.meetup_db = meetup_list
            return self.meetup_db
        elif self.db == 'question':
            self.question_db = question_list
            return self.question_db


    def check_exists(self, data):
        db = self.check_db()
        for item in db:
            if item['name'] == data:
                return jsonify({"status_code" : 409, "error" : "Conflict: Already Exists"}),409
            else:
                return jsonify({"status_code" : 200, "message" : "Ok"}),200    


    def return_data(self):
        db = self.check_db()
        return db

    