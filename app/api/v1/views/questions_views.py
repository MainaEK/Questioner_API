'''from flask import Flask, jsonify, request, Response, json
from ..models.question_models import QuestionModel
from ...v1 import v1 
from ..utils.validations import sanitize_input_questions


class QuestionEndpoints(QuestionModel):
    def __init__(self):
        self.db = QuestionModel
        
    @v1.route('/questions', methods=['POST'])
    def create_question(self):
        data = request.get_json() ['question']
        response = self.db.save(data)
        if not response:
            return jsonify({'status' : 400,'error' : 'Bad Request'}),400
        else:
            return jsonify ({'status' : 201,'data' : response}),201 '''