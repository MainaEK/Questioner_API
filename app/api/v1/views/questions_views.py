from flask import Flask, jsonify, request, Response, json
from ..models.question_models import questions
from ...v1 import v1 
from ..utils.validations import sanitize_input_questions

@v1.route('/questions', methods=['POST'])
def create_question():
    request_data = request.get_json()
    if(sanitize_input_questions(request_data)):
        new_question = {
            'id_' : request_data['id_'],
            'createdOn' : request_data['createdOn'],
            'createdBy' : request_data['createdBy'],
            'meetup' : request_data['meetup'],
            'title' : request_data['title'],
            'body' : request_data['body'],
            'votes': request_data['votes']
        }
        questions.append(new_question)
        return jsonify({'status' : 201,'data' : new_question}),201
    else:
        return jsonify({'status' : 400,'error' : 'Invalid Question passed'}),400