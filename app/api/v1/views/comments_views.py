from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError
from ..models.question_models import QuestionModel
from ..Schemas.comment_schema import CommentSchema
from ...v1 import v1

@v1.route('/comments', methods=['POST'])
def make_comment():
    json_data = request.get_json()

    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    data, errors = CommentSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))

    elif not QuestionModel().check_exists("q_id",json_data['q_id']):
        abort(make_response(jsonify({'status' : 404,'message' : 'Question not found'}),404))


    response = QuestionModel().find('q_id',json_data['q_id'])
    return jsonify({'status' : 201,'data' : [{'q_id' : response['q_id'], 'title' : response['title'],
    'body': response['body'], 'comment' : json_data['comment']}]}),201
    