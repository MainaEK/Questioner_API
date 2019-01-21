from .base_models import BaseModels
from ....database import db_con


class CommentsModel(BaseModels):
    def __init__(self):
        super().__init__('comments')
    
        
    def create_comment(self, comment):
        self.cur = self.connect.cursor()
        query = """INSERT INTO comments (body,question_id,user_id)\
        VALUES ('{}','{}','{}') RETURNING json_build_object('question_id',question_id,'body',body)
        ;""".format(comment['body'],comment['question_id'],comment['user_id'])
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result