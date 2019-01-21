from .base_models import BaseModels
from ....database import db_con


class QuestionModel(BaseModels):
    def __init__(self):
        super().__init__('questions')
    
        
    def create_question(self, question):
        self.cur = self.connect.cursor()
        query = """INSERT INTO questions (user_id,meetup_id,title,body)\
        VALUES ('{}','{}','{}','{}') RETURNING json_build_object('user_id',user_id,'meetup_id',meetup_id,'title',title,'body',body)
        ;""".format(question['user_id'],question['meetup_id'],question['title'],question['body'])
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result