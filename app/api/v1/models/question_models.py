from datetime import datetime
from ..utils.generator import generator

questions = []

class QuestionModel(object):
    """ Model class for the question object """

    def __init__(self):
        self.db = questions

    def save(self, question ={"q_id" : "", "created_on" : "", "created_by":"", "meetup":"",
                 "title":"", "body":"", "votes": 0}):
        """ Function to save new question """
        super().__init__(q_id = generate_id, created_on = datetime())
        self.db.append(question)
        return self.db
        

    def fetch_using_id(self, q_id):
        """ Function to fetch questions by ID """
        fetched_questions = [question for question in self.db if question['q_id'] == q_id]
        return fetched_questions[0]

    def all(self):
        """ Function to fetch all questions """
        return self.db