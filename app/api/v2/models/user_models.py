from werkzeug.security import generate_password_hash

from .base_models import BaseModels


class UserModel(BaseModels):
    def __init__(self):
        super().__init__('users')

    def check_exist(self, key, value):
        self.cur = self.connect.cursor()
        query = """SELECT * FROM users WHERE {} = '{}';""".format(key, value)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return  len(result) > 0


    def create_user(self, user):
        self.cur = self.connect.cursor()
        password = generate_password_hash(user['password'])
        query = """INSERT INTO users (firstname,lastname,othername,email,phone_number,username,password)\
        VALUES ('{}','{}','{}','{}','{}','{}','{}')\
        RETURNING json_build_object('user_id',user_id,'firstname',firstname,'lastname',lastname,'email',email,'phone_number',phone_number,'username', username)
        ;""".format(user['firstname'],user['lastname'],user['othername'],user['email'],user['phone_number'],user['username'], password)
        self.cur.execute(query)
        self.connect.commit()
        result = self.cur.fetchone()
        return result
