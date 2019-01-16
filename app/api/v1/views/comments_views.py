# third party imports
from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError

# local imports
from ..models.question_models import QuestionModel
from ..Schemas.comment_schema import CommentSchema
from ...v1 import v1

@v1.route('/comments', methods=['POST'])
def make_comment():
    """ For making comments on questions"""
    json_data = request.get_json()

    """ Checks if data has been provided and in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    """Checks to see if all the required fields are filled"""
    data, errors = CommentSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))
        
        """Checks if the question exists in the db"""
    elif not QuestionModel().check_exists("q_id",json_data['q_id']):
        abort(make_response(jsonify({'status' : 404,'message' : 'Question not found'}),404))

        """Finds the specific question and returns data in json format"""
    response = QuestionModel().find('q_id',json_data['q_id'])
    return jsonify({'status' : 201,'data' : [{'q_id' : response['q_id'], 'title' : response['title'],
    'body': response['body'], 'comment' : json_data['comment']}]}),201
    