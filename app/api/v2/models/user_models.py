"""
This module defines the user model and associated functions
"""
from werkzeug.security import generate_password_hash

from .base_models import BaseModels


class UserModel(BaseModels):
    """
    This class encapsulates the functions of the user model
    """

    def __init__(self):
        """Initializes database"""
        super().__init__('users')

    def check_exist(self, key, value):
        """
        Function to check for similar email or username already registered
        """
        query = """SELECT * FROM users WHERE {} = '{}';""".format(key, value)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return len(result) > 0

    def find(self, value):
        """
        Function to find a particular user and return data about them
        """
        query = """SELECT user_id,firstname,lastname,email,username,password FROM users WHERE username = '{}';""".format(value)
        self.cur.execute(query)
        result = self.cur.fetchone()
        print(result)
        return result

    def create_user(self, user):
        """Function to create a new user"""
        password = generate_password_hash(user['password'])
        query = """INSERT INTO users (firstname,lastname,othername,email,phone_number,username,password)\
        VALUES ('{}','{}','{}','{}','{}','{}','{}')\
        RETURNING user_id,firstname,lastname,email,phone_number,username
        ;""".format(user['firstname'], user['lastname'], user['othername'], user['email'], user['phone_number'], user['username'], password)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result
