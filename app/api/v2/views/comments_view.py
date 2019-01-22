# third party imports
from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError
from flask_jwt_extended import (jwt_required, get_jwt_identity)

# local imports
from ..models.comments_model import CommentsModel
from ..Schemas.comment_schema import CommentSchema
from ...v2 import v2

@v2.route('/questions/<int:q_id>/comments', methods=['POST'])
@jwt_required
def create_comments(q_id):
    """ Endpoint that creates a new comment"""
    json_data = request.get_json()
    
    """ Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
    
    """ Checks that all the required fields have input"""
    data, errors = CommentSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))

    """ Creates the meetup and returns feedback in json format"""
    user_id = get_jwt_identity()
    result = CommentsModel().create_comment(user_id, q_id, json_data)
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': result}), 201