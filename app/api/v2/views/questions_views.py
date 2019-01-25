"""
This contains the endpoints for questions
"""
from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError
from flask_jwt_extended import (jwt_required, get_jwt_identity)

# local imports
from ..models.question_models import QuestionModel
from ..models.meetups_models import MeetupModel
from ..schemas.question_schema import QuestionSchema
from ...v2 import v2


@v2.route('/meetups/<int:m_id>/questions', methods=['POST'])
@jwt_required
def create_question(m_id):
    """Endpoint to create a question"""
    json_data = request.get_json()

    """Checks to see if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(
            jsonify({'status': 400, 'message': 'Sorry but the data provided should be in json'}), 400))

    """Checks if all required fields have been filled"""
    data, errors = QuestionSchema().load(json_data)
    if errors:
        abort(make_response(jsonify(
            {'status': 400, 'message': 'Empty field. Please fill in all required fields', 'errors': errors}), 400))

    '''Checks if the meetup exists'''
    if not MeetupModel().check_exists('meetup_id', m_id):
        abort(make_response(
            jsonify({'status': 404, 'message': 'Sorry but the meetup being posted to does not exist'}), 404))

    """Posts the question and returns feedback in json format"""
    user_id = get_jwt_identity()
    result = QuestionModel().create_question(user_id, m_id, json_data)
    return jsonify({'status': 201, 'message': 'Question was posted successfully', 'data': result}), 201


@v2.route('/questions/<int:q_id>/upvote', methods=['PATCH'])
@jwt_required
def upvote_question(q_id):
    """Checks if the question exists"""
    if not QuestionModel().check_exists("question_id", q_id):
        abort(make_response(
            jsonify({'status': 404, 'message': 'Sorry but this question does not exist'}), 404))

    """Upvotes the question and returns feedback in json format"""
    question = QuestionModel().upvote(q_id)
    return jsonify({'status': 200, 'message': 'Question upvoted successfully', 'data': question}), 200


@v2.route('/questions/<int:q_id>/downvote', methods=['PATCH'])
@jwt_required
def downvote_question(q_id):
    """Checks if the question exists"""
    if not QuestionModel().check_exists("question_id", q_id):
        abort(make_response(
            jsonify({'status': 404, 'message': 'Sorry but this question does not exist'}), 404))

    """Downvotes the question and returns feedback in json format"""
    question = QuestionModel().downvote(q_id)
    return jsonify({'status': 200, 'message': 'Question downvoted successfully', 'data': question}), 200
