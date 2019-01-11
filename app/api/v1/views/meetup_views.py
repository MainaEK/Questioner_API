from flask import Flask, json, jsonify, Response, request
from ..models.meetup_models import MeetupModel
from ...v1 import v1
from ..schemas.meetup_schema import MeetupSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

db = MeetupModel()

class MeetupEndpoints():
    def __init__(self):
        self.db = MeetupModel() 

    @v1.route('/meetups/upcoming' , methods =['GET'])
    def get_all_meetups():
        meetups = db.get_all()
        result = MeetupSchema(many=True).dump(meetups).data
        return jsonify({'status' : 200 , 'data' : result}),200
