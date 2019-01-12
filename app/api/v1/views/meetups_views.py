from flask import Flask, jsonify, request, Response, json
from ..models.meetups_models import MeetupModel
from ...v1 import v1
from ..utils.validations import sanitize_input


@v1.route('/meetups/upcoming', methods=['GET'])
def get_all_meetups():
    response = MeetupModel().get_all()
    return jsonify({'status' : 200,'data' : response}),200


'''@v1.route('/meetups/<int:id_>', methods=['GET'])
def get_specific_meetup(id_):
    val = {}
    for meetup in meetups:
        if meetup['id_'] == id_:
            val = {
                'id_' : meetup['id_'],
                'createdOn' : meetup['createdOn'],
                'location' : meetup['location'],
                'images' : meetup['images'],
                'topic' : meetup['topic'],
                'happeningOn' : meetup['happeningOn'],
                'tags': meetup['tags']
            }
            return jsonify ({'status' : 201,'data' : val}),201 
        else:
            return jsonify({'status' : 404,'error' : 'Not Found'}),404



@v1.route('/meetups', methods=['POST'])
def create_meetup():
    request_data = request.get_json()
    if(sanitize_input(request_data)):
        new_meetup = {
            'id_' : request_data['id_'],
            'createdOn' : request_data['createdOn'],
            'location' : request_data['location'],
            'images' : request_data['images'],
            'topic' : request_data['topic'],
            'happeningOn' : request_data['happeningOn'],
            'tags': request_data['tags']
        }
        meetups.append(new_meetup)
        return jsonify({'status' : 201,'data' : new_meetup}),201
    else:
        return jsonify({'status' : 400,'error' : 'Invalid Meetup passed'}),400'''