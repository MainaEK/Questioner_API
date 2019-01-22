from .base_models import BaseModels


class RsvpModel(BaseModels):
    def __init__(self):
        super().__init__('rsvps')
    
        
    def create_rsvp(self, user_id, m_id, rsvp):
        self.cur = self.connect.cursor()
        query = """WITH inserted AS (INSERT INTO rsvps (user_id,meetup_id,rsvp)\
        VALUES ('{}','{}','{}') RETURNING rsvp,meetup_id)\
        SELECT json_build_object('rsvp',rsvp,'meetup_id',meetup_id,'topic',topic)\
        FROM (SELECT inserted.rsvp,meetups.meetup_id,meetups.topic FROM inserted INNER JOIN meetups ON inserted.meetup_id = meetups.meetup_id) AS returned
        ;""".format(user_id,m_id,rsvp)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result