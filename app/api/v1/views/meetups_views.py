from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError
from ..models.meetups_models import MeetupModel
from ..Schemas.meetup_schema import MeetupSchema
from ..Schemas.tag_schema import TagSchema
from ...v1 import v1



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

    data, errors = MeetupSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))


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
        'status': 201,
        'message': 'Meetup rsvp successfully',
        'data': {
            'm_id': meetup['m_id'],
            'topic' : meetup['topic'],
            'status': rsvps
        }
    }), 201

@v1.route('/meetups/<int:m_id>', methods=['DELETE'])
def delete_meetup(m_id):
    '''Checks if the m_id exists in the db'''
    if not MeetupModel().check_exists("m_id",m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))
        
    '''If the m_id exists it is then deleted''' 
    MeetupModel().delete('m_id',m_id)
    if not MeetupModel().check_exists("m_id",m_id):
        return jsonify({'status' : 200,'data' : [], 'message' : 'Successfully deleted'}),200

@v1.route('/meetups/<int:m_id>/tags', methods=['POST'])
def add_tags(m_id):
    json_data = request.get_json()

    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    data, errors = TagSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))

    elif not MeetupModel().check_exists("m_id",m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))


    response = MeetupModel().find('m_id',m_id)
    return jsonify({'status' : 201,'data' : [{'m_id' : response['m_id'], 'topic' : response['topic'], 
    'tags' : json_data['tags']}]}),201
