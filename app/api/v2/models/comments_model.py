"""
This module defines the comments model and associated functions
"""
from .base_models import BaseModels
from ....database import db_con


class CommentsModel(BaseModels):
    """
    This class encapsulates the functions of the comments model
    """

    def __init__(self):
        """Initialize the database"""
        super().__init__('comments')

    def create_comment(self, user_id, q_id, comment):
        """
        Function that creates a comment and posts it to a certain question(q_id) 
        tied to a particular user(user_id)
        """
        self.cur = self.connect.cursor()
        query = """WITH inserted AS (INSERT INTO comments (comment,question_id,user_id)\
        VALUES ('{}','{}','{}') RETURNING comment,question_id)\
        SELECT json_build_object('question_id', question_id,'title', title,'body', body,'comment',comment)\
        FROM (SELECT inserted.comment, questions.question_id, questions.title, questions.body FROM inserted INNER JOIN questions ON inserted.question_id = questions.question_id) AS returned
        ;""".format(comment['comment'], q_id, user_id)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result

    def check_similar_comment(self, user_id, q_id, comment):
        """Function to check for similar meetups 
        already in the database
        """
        self.cur = self.connect.cursor()
        query = """SELECT * FROM comments WHERE user_id = {} AND question_id = {} AND comment = '{}';""".format(
            user_id, q_id, comment)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return len(result) > 0
