from flask import Flask, jsonify, request, Response, json
from ..models.meetups_models import meetups
from ...v1 import v1
from ..utils.validations import sanitize_input


@v1.route('/meetups', methods=['GET'])
def get_all_meetups():
    return jsonify({'status' : 201,'data' : meetups,}),201


@v1.route('/meetups/<string:topic>', methods=['GET'])
def get_specific_meetup(topic):
    val = {}
    for meetup in meetups:
        if meetup['topic'] == topic:
            val = {
                'id_' : meetup['id_'],
                'createdOn' : meetup['createdOn'],
                'location' : meetup['location'],
                'images' : meetup['images'],
                'topic' : meetup['topic'],
                'happeningOn' : meetup['happeningOn'],
                'tags': meetup['tags']
            }
    return jsonify (val)    

