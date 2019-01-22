from marshmallow import Schema, fields
from ..utils.validations import Not_null_string,password_check


class UserSchema(Schema):
    """ Class to validate schema for User object """

    firstname = fields.Str(required=True, validate = Not_null_string)
    lastname= fields.Str(required=True, validate= Not_null_string)
    othername = fields.Str(required=False)
    email = fields.Email(required=True, validate= Not_null_string)
    phone_number = fields.Int(required=True)
    username = fields.Str(required=True)
    registered_on = fields.Date(required=True, validate= Not_null_string)
    password= fields.Str(required=True, validate= password_check)