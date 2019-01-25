"""
This contains the endpoints for comments
"""
# third party imports
from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError
from flask_jwt_extended import (jwt_required, get_jwt_identity)

# local imports
from ..models.comments_model import CommentsModel
from ..models.question_models import QuestionModel
from ..schemas.comment_schema import CommentSchema
from ...v2 import v2


@v2.route('/questions/<int:q_id>/comments', methods=['POST'])
@jwt_required
def create_comments(q_id):
    """ Endpoint that creates a new comment"""
    json_data = request.get_json()

    """ Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(
            jsonify({'status': 400, 'message': 'Sorry but the data provided should be in json'}), 400))

    """ Checks that all the required fields have input"""
    data, errors = CommentSchema().load(json_data)
    if errors:
        abort(make_response(jsonify(
            {'status': 400, 'message': 'Empty field. Please fill in all required fields', 'errors': errors}), 400))

    """Checks whether the question exists"""
    if not QuestionModel().check_exists('question_id', q_id):
        abort(make_response(
            jsonify({'status': 404, 'message': 'Sorry but this question does not exist'}), 404))

    '''Checks if a similar comment exists'''
    user_id = get_jwt_identity()
    if CommentsModel().check_similar_comment(user_id, q_id, json_data['comment']):
        abort(make_response(
            jsonify({'status': 400, 'message': 'Similar comment found from the same user to the same question'}), 400))

    """ Creates the meetup and returns feedback in json format"""
    user_id = get_jwt_identity()
    result = CommentsModel().create_comment(user_id, q_id, json_data)
    return jsonify({'status': 201, 'message': 'Comment was made successfully', 'data': result}), 201
