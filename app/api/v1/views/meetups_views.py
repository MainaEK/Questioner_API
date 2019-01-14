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
    if not MeetupModel().check_exists("m_id",m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))
        
    '''If the m_id exists it is then returned''' 
    response = MeetupModel().find('m_id',m_id)
    return jsonify({'status' : 200,'data' : response}),200

    
@v1.route('/meetups', methods=['POST'])
def create_meetup():
    json_data = request.get_json()

    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    result = MeetupModel().create_meetup(json_data)
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': result}), 201

@v1.route('/meetups/<int:m_id>/<string:rsvps>', methods=['POST'])
def rspvs_meetup(m_id, rsvps):
    """ Endpoint to RSVP to meetup """
    valid_responses = ('yes', 'no', 'maybe')

    """Check if meetup exists"""
    if not MeetupModel().check_exists('m_id', m_id):
        abort(make_response(jsonify({'status': 404, 'message': 'Meetup not found'}), 404))

    """Check if rsvp is valid"""
    if rsvps not in valid_responses:
        abort(make_response(jsonify({'status': 400, 'message': 'Invalid rsvp'}), 400))

    meetup = MeetupModel().find('m_id', m_id)
    return jsonify({
        'status': 200,
        'message': 'Meetup rsvp successfully',
        'data': {
            'user_id': meetup('user_id'),
            'm_id': meetup['m_id'],
            'topic' : meetup['topic'],
            'status': rsvps
        }
    }), 200

