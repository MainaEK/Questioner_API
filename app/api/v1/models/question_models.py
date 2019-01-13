from datetime import datetime
from ..utils.generator import generate_id
from .base_models import BaseModels


class QuestionModel(BaseModels):
    def __init__(self):
        super().__init__('question')
    
        
    def create_question(self, question):
        question = {
            'q_id' : question['q_id'],
            'created_on' : question['created_on'],
            'created_by' : question['created_by'],
            'images' : question['images'],
            'title' : question['title'],
            'body' : question['body'],
            'votes': question['votes']
        }
        response = self.save(question)
        return response
        