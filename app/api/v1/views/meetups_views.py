from flask import Flask, jsonify, request, Response, json, make_response
from ..models.meetups_models import MeetupModel
from ...v1 import v1
from ..utils.validations import sanitize_input


class MeetupEndpoints(MeetupModel):
    def __init__(self):
        self.db = MeetupModel

    @v1.route('/meetups/upcoming', methods=['GET'])
    def get_all_meetups(self):
        response = self.db.get_all()
        if not response:
            return jsonify({'status' : 404,'error' : 'Not Found'}),404
        else:
            return jsonify({'status' : 201,'data' : response}),201
            
    
    @v1.route('/meetups/<int:m_id>', methods=['GET'])
    def get_specific_meetup(self, m_id):
        response = self.db.fetch_using_id()
        if not response:
            return jsonify({'status' : 404,'error' : 'Not Found'}),404
        else:
            return jsonify ({'status' : 201,'data' : response}),201 
            
    
    @v1.route('/meetups', methods=['POST'])
    def create_meetup(self):
        data = request.get_json() ['meetup']
        response = self.db.save(data)
        if not response:
            return jsonify({'status' : 400,'error' : 'Bad Request'}),400
        else:
            return jsonify ({'status' : 201,'data' : response}),201 