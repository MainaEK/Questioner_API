# third party imports
from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError

# local imports
from ..models.comments_model import CommentsModel
from ..Schemas.comment_schema import CommentSchema
from ...v2 import v2

@v2.route('/comments', methods=['POST'])
def create_comments():
    """ Endpoint that creates a new comment"""
    json_data = request.get_json()
    
    """ CHecks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
    
    """ Checks that all the required fields have input"""
    data, errors = CommentSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))

    """ Creates the meetup and returns feedback in json format"""
    result = CommentsModel().create_comment(json_data)
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': result}), 201