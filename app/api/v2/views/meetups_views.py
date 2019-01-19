# third party imports
from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError

# local imports
from ..models.meetups_models import MeetupModel
from ..Schemas.meetup_schema import MeetupSchema
from ..Schemas.tag_schema import TagSchema
from ..Schemas.image_schema import ImageSchema
from ...v1 import v1



@v1.route('/meetups/upcoming', methods=['GET'])
def get_all_meetups():
    '''Gets all upcoming meetups'''
    response = MeetupModel().get_all()
    return jsonify({'status' : 200,'data' : response}),200

@v1.route('/meetups/<int:m_id>', methods=['GET'])
def get_specific_meetup(m_id):
    '''Checks if the meetup exists'''
    if not MeetupModel().check_exists("m_id",m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))
        
    '''If the m_id exists it is then returned''' 
    response = MeetupModel().find('m_id',m_id)
    return jsonify({'status' : 200,'data' : response}),200

    
@v1.route('/meetups', methods=['POST'])
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
    result = MeetupModel().create_meetup(json_data)
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': result}), 201

@v1.route('/meetups/<int:m_id>/<string:rsvps>', methods=['POST'])
def rspvs_meetup(m_id, rsvps):
    """ Endpoint to RSVP to meetup """
    valid_responses = ('yes', 'no', 'maybe')

    """Checks if meetup exists"""
    if not MeetupModel().check_exists('m_id', m_id):
        abort(make_response(jsonify({'status': 404, 'message': 'Meetup not found'}), 404))

    """Check if rsvp is valid"""
    if rsvps not in valid_responses:
        abort(make_response(jsonify({'status': 400, 'message': 'Invalid rsvp'}), 400))
    
    """Creates the RSVP and returns feedback in json format"""
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
    '''Checks if the meetup exists'''
    if not MeetupModel().check_exists("m_id",m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))
        
    '''If the meetup exists it is then deleted and feedback returned ''' 
    MeetupModel().delete('m_id',m_id)
    if not MeetupModel().check_exists("m_id",m_id):
        return jsonify({'status' : 200,'data' : [], 'message' : 'Successfully deleted'}),200

@v1.route('/meetups/<int:m_id>/tags', methods=['POST'])
def add_tags(m_id):
    """ Endpoint that adds tags"""
    json_data = request.get_json()
    
    """Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
    
    """Checks if the required fields have been filled"""
    data, errors = TagSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))
    
        """Checks if the meetup exists"""
    elif not MeetupModel().check_exists("m_id",m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))

        """If the meetup exists it adds the tags and returns feedback"""
    response = MeetupModel().find('m_id',m_id)
    return jsonify({'status' : 201,'data' : [{'m_id' : response['m_id'], 'topic' : response['topic'], 
    'tags' : json_data['tags']}]}),201

@v1.route('/meetups/<int:m_id>/images', methods=['POST'])
def add_images(m_id):
    """ Endpoint that adds images"""
    json_data = request.get_json()
    
    """Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
    
    """Checks if the required fields have been filled"""  
    data, errors = ImageSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))
    
        """Checks if the meetup exists"""
    elif not MeetupModel().check_exists("m_id",m_id):
        abort(make_response(jsonify({'status' : 404,'message' : 'Meetup not found'}),404))

        """If the meetup exists it adds the tags and returns feedback"""
    response = MeetupModel().find('m_id',m_id)
    return jsonify({'status' : 201,'data' : [{'m_id' : response['m_id'], 'topic' : response['topic'], 
    'images' : json_data['images']}]}),201
