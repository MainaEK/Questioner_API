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

    @v1.route('/meetups', methods=['POST'])
    def create_meetup():
        """ Function to create meetup """
        json_data = request.get_json()

        ''' If no data has been provided'''
        if not json_data:
            return jsonify({'status': 400, 'error': 'No data provided'}), 400

        '''Checks if request is valid'''
        data, errors = MeetupSchema().load(json_data)
        if errors:
            return jsonify({'status': 400, 'error' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400

        '''Saves the new meetup and returns response'''
        new_meetup = db.create(data)
        result = MeetupSchema().dump(new_meetup).data
        return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': [result]}), 201