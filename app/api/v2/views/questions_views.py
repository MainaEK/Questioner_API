from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError

# local imports
from ..models.question_models import QuestionModel
from ..Schemas.question_schema import QuestionSchema
from ...v2 import v2



@v2.route('/questions', methods=['POST'])
def create_question():
    """Endpoint to create a question"""
    json_data = request.get_json()
    
    """Checks to see if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    """Checks if all required fields have been filled"""
    data, errors = QuestionSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))

    """Posts the question and returns feedback in json format"""     
    result = QuestionModel().create_question(json_data)
    return jsonify({'status': 201, 'message': 'Question was posted successfully', 'data': result}), 201