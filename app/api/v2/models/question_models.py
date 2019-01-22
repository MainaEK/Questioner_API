from .base_models import BaseModels



class QuestionModel(BaseModels):
    def __init__(self):
        super().__init__('questions')
    
        
    def create_question(self, user_id, m_id, question):
        self.cur = self.connect.cursor()
        query = """INSERT INTO questions (user_id,meetup_id,title,body)\
        VALUES ('{}','{}','{}','{}') RETURNING json_build_object('user_id',user_id,'meetup_id',meetup_id,'question_id',question_id,'title',title,'body',body)
        ;""".format(user_id,m_id,question['title'],question['body'])
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result

    def upvote(self, q_id):
        self.cur = self.connect.cursor()
        query = """UPDATE questions SET votes = votes + 1 WHERE question_id = {} RETURNING json_build_object('meetup_id',meetup_id,'title',title,'body',body,'votes',votes) ;""".format(q_id)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result

    def downvote(self, q_id):
        self.cur = self.connect.cursor()
        query = """UPDATE questions SET votes = votes - 1 WHERE question_id = {} RETURNING json_build_object('meetup_id',meetup_id,'title',title,'body',body,'votes',votes) ;""".format(q_id)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result