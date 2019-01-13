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