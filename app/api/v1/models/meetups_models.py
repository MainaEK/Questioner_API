from datetime import datetime
from ..utils.generator import generate_id
from .base_models import BaseModels


class MeetupModel(BaseModels):
    def __init__(self):
        super().__init__('meetup')
        
    def get_all(self):
        response = self.db.return_data()
        return response


    '''def save(self, name, email):
        user = {
            'name' : name
            'email' : email
        }
        _b_model = BaseModel()'''