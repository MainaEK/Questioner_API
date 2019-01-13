from flask import Flask, jsonify, request, Response, json, abort, make_response
from ..models.meetups_models import MeetupModel
from ...v1 import v1
from ..utils.validations import sanitize_input


@v1.route('/meetups/upcoming', methods=['GET'])
def get_all_meetups():
    '''Gets all upcoming meetups'''
    response = MeetupModel().get_all()
    return jsonify({'status' : 200,'data' : response}),200

@v1.route('/meetups/<int:m_id>', methods=['GET'])
def get_specific_meetup(m_id):
    '''Checks if the m_id exists in the db'''
    if not MeetupModel().check_exists('m_id',m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))
    '''If the m_id exists it is then returned''' 
    response = MeetupModel().find('m_id',m_id)
    return jsonify({'status' : 200,'data' : response}),200

    
@v1.route('/meetups', methods=['POST'])
def create_meetup():
    json_data = request.get_json()

    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    result = MeetupModel().save(json_data)
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': result}), 201

