# third party imports
from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError

# local imports
from ..models.meetups_models import MeetupModel
from ..models.rsvp_models import RsvpModel
from ..Schemas.meetup_schema import MeetupSchema
from ...v2 import v2



@v2.route('/meetups/upcoming', methods=['GET'])
def get_all_meetups():
    '''Gets all upcoming meetups'''
    response = MeetupModel().get_all()
    return jsonify({'status' : 200,'data' : response}),200

@v2.route('/meetups', methods=['POST'])
def create_meetup():
    """ Endpoint that creates a new meetup"""
    json_data = request.get_json()
    
    """ CHecks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
    
    """ Checks that all the required fields have input"""
    data, errors = MeetupSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))

    """ Creates the meetup and returns feedback in json format"""
    print(json_data)
    result = MeetupModel().create_meetup(json_data)
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': result}), 201


@v2.route('/meetups/<int:m_id>', methods=['GET'])
def get_specific_meetup(m_id):
    '''Checks if the meetup exists'''
    if not MeetupModel().check_exists('meetup_id', m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))
        
    '''If the m_id exists it is then returned''' 
    response = MeetupModel().find(m_id)
    return jsonify({'status' : 200,'data' : response}),200
    
@v2.route('/meetups/<int:m_id>', methods=['DELETE'])
def delete_meetup(m_id):
    '''Checks if the meetup exists'''
    if not MeetupModel().check_exists("meetup_id",m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))
        
    '''If the meetup exists it is then deleted and feedback returned ''' 
    MeetupModel().delete(m_id)
    if not MeetupModel().check_exists("meetup_id",m_id):
        return jsonify({'status' : 200,'data' : [], 'message' : 'Successfully deleted'}),200

@v2.route('/meetups/<int:m_id>/<string:rsvp>', methods=['POST'])
def rspvs_meetup(m_id, rsvp):
    """ Endpoint to RSVP to meetup """
    valid_responses = ('yes', 'no', 'maybe')

    """Checks if meetup exists"""
    if not MeetupModel().check_exists('meetup_id', m_id):
        abort(make_response(jsonify({'status': 404, 'message': 'Meetup not found'}), 404))

    """Check if rsvp is valid"""
    if rsvp not in valid_responses:
        abort(make_response(jsonify({'status': 400, 'message': 'Invalid rsvp'}), 400))
    
    """Creates the RSVP and returns feedback in json format"""
    response = RsvpModel().create_rsvp(m_id,rsvp)
    return jsonify({'status' : 201,'message' : 'Rsvp made.','data' : response}),201

