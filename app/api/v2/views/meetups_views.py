"""
This contains the endpoints for meetups
"""
# third party imports
from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError
from flask_jwt_extended import (jwt_required, get_jwt_identity)

# local imports
from ..models.meetups_models import MeetupModel
from ..models.rsvp_models import RsvpModel
from ..schemas.meetup_schema import MeetupSchema
from ...v2 import v2


@v2.route('/meetups/upcoming', methods=['GET'])
def get_all_meetups():
    '''Gets all upcoming meetups'''
    response = MeetupModel().get_all()
    return jsonify({'status': 200, 'data': response}), 200


@v2.route('/meetups', methods=['POST'])
@jwt_required
def create_meetup():
    """Checks to see if the user is the admin"""
    user_id = get_jwt_identity()
    if not user_id == 1:
        abort(make_response(
            jsonify({'status': 401, 'message': 'Unauthorized for current user'}), 401))

        """ Endpoint that creates a new meetup"""
    json_data = request.get_json()

    """ Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(
            jsonify({'status': 400, 'message': 'Sorry but the data provided should be in json'}), 400))

    """ Checks that all the required fields have input"""
    data, errors = MeetupSchema().load(json_data)
    if errors:
        abort(make_response(jsonify(
            {'status': 400, 'message': 'Empty. Please fill in all required fields', 'errors': errors}), 400))

    '''Checks if a similar meetup exists'''
    if MeetupModel().check_similar(json_data['topic'], json_data['location'], json_data['happening_on']):
        abort(make_response(
            jsonify({'status': 400, 'message': 'Similar meetup found with similar topic, location and happening_date'}), 400))

    """ Creates the meetup and returns feedback in json format"""
    result = MeetupModel().create_meetup(json_data)
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': result}), 201


@v2.route('/meetups/<int:m_id>', methods=['GET'])
def get_specific_meetup(m_id):
    '''Checks if the meetup exists'''
    if not MeetupModel().check_exists('meetup_id', m_id):
        abort(make_response(
            jsonify({'status': 404, 'message': 'Sorry but this meetup does not exist'}), 404))

    '''Finds the meetup'''
    response = MeetupModel().find(m_id)
    return jsonify({'status': 200, 'data': response}), 200


@v2.route('/meetups/<int:m_id>', methods=['DELETE'])
@jwt_required
def delete_meetup(m_id):
    """Checks if the user is the admin"""
    user_id = get_jwt_identity()
    if not user_id == 1:
        abort(make_response(
            jsonify({'status': 401, 'message': 'Unauthorized for current user'}), 401))

        '''Checks if the meetup exists'''
    if not MeetupModel().check_exists("meetup_id", m_id):
        abort(make_response(
            jsonify({'status': 404, 'message': 'Sorry but this meetup does not exist'}), 404))

    '''If the meetup exists it is then deleted and feedback returned '''
    MeetupModel().delete(m_id)
    if not MeetupModel().check_exists("meetup_id", m_id):
        return jsonify({'status': 200, 'data': [], 'message': 'Meetup successfully deleted'}), 200


@v2.route('/meetups/<int:m_id>/<string:rsvp>', methods=['POST'])
@jwt_required
def rsvps_meetup(m_id, rsvp):
    """ Endpoint to RSVP to a meetup """
    valid_responses = ('yes', 'no', 'maybe')

    """Checks if meetup exists"""
    if not MeetupModel().check_exists('meetup_id', m_id):
        abort(make_response(
            jsonify({'status': 404, 'message': 'Sorry but this meetup does not exist'}), 404))

    """Check if rsvp is valid"""
    if rsvp not in valid_responses:
        abort(make_response(
            jsonify({'status': 400, 'message': 'Invalid rsvp. Choose between (yes, no, maybe)'}), 400))

    """Creates the RSVP and returns feedback in json format"""
    user_id = get_jwt_identity()
    response = RsvpModel().create_rsvp(user_id, m_id, rsvp)
    return jsonify({'status': 201, 'message': 'The rsvp has been made.', 'data': response}), 201
