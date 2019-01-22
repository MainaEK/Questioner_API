from .base_models import BaseModels


class RsvpModel(BaseModels):
    def __init__(self):
        super().__init__('rsvps')
    
        
    def create_rsvp(self, m_id, rsvp):
        self.cur = self.connect.cursor()
        query = """INSERT INTO rsvps (meetup_id,rsvp)\
        VALUES ('{}','{}') RETURNING json_build_object('meetup_id',meetup_id,'topic',topic,'rsvp',rsvp)
        ;""".format(m_id,rsvp)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result