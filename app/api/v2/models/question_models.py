from datetime import datetime

from .base_models import BaseModels


class QuestionModel(BaseModels):
    def __init__(self):
        super().__init__('question')
    
        
    def create_question(self, question):
        question = {
            'q_id' : question['q_id'],
            'created_on' : question['created_on'],
            'created_by' : question['created_by'],
            'meetup' : question['meetup'],
            'title' : question['title'],
            'body' : question['body'],
            'votes': question['votes']
        }
        response = self.save(question)
        return response

    def upvote(self, q_id):
        self.db = BaseModels(db = 'question')
        response = self.db.return_data()


        """ Function to upvote question """
        for question in response:
            if question['q_id'] == q_id:
                question['votes'] = question['votes']+1

            return question

    def downvote(self, q_id):
        self.db = BaseModels(db = 'question')
        response = self.db.return_data()

        """ Function to downvote question """
        for question in response:
            if question['q_id'] == q_id:
                question['votes'] = question['votes']-1

            return question
        
        