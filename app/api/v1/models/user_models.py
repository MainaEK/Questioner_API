from datetime import datetime

from .base_models import BaseModels

class UserModel(BaseModels):
    def __init__(self):
        super().__init__('user')

    def create_user(self, user):
        user = {
            'user_id' : user['user_id'],
            'firstname' : user['firstname'],
            'lastname' : user['lastname'],
            'othername' : user['othername'],
            'email' : user['email'],
            'phone_number' : user['phone_number'],
            'username': user['username'],
            'registered_on': user['registered_on'],
            'password' : user['password']
        }
        response = self.save(user)
        return response

  
        