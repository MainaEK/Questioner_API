from flask import Flask, jsonify, request, Response, json, abort, make_response
from ..models.question_models import QuestionModel
from ...v1 import v1
from ..utils.validations import sanitize_input


@v1.route('/questions', methods=['POST'])
def create_question():
    json_data = request.get_json()

    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    result = QuestionModel().create_question(json_data)
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': result}), 201

@v1.route('/questions/<int:q_id>/upvote', methods=['PATCH'])
def upvote_question(q_id):
    if not QuestionModel().check_exists("q_id",q_id):
        abort(make_response(jsonify({'status': 404, 'message': 'Question not found'}), 404))

    question = QuestionModel().upvote(q_id)
    return jsonify({'status': 200, 'message': 'Question upvoted successfully', 'data': question}), 200

@v1.route('/questions/<int:q_id>/downvote', methods=['PATCH'])
def downvote_question(q_id):
    if not QuestionModel().check_exists("q_id",q_id):
        abort(make_response(jsonify({'status': 404, 'message': 'Question not found'}), 404))

    question = QuestionModel().downvote(q_id)
    return jsonify({'status': 200, 'message': 'Question downvoted successfully', 'data': question}), 200