from .base_models import BaseModels
from ....database import db_con


class CommentsModel(BaseModels):
    def __init__(self):
        super().__init__('comments')
    
        
    def create_comment(self, user_id, q_id, comment):
        self.cur = self.connect.cursor()
        query = """WITH inserted AS (INSERT INTO comments (comment,question_id,user_id)\
        VALUES ('{}','{}','{}') RETURNING comment,question_id)\
        SELECT json_build_object('question_id', question_id,'title', title,'body', body,'comment',comment)\
        FROM (SELECT inserted.comment, questions.question_id, questions.title, questions.body FROM inserted INNER JOIN questions ON inserted.question_id = questions.question_id) AS returned
        ;""".format(comment['comment'],q_id,user_id)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result