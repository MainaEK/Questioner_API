
from marshmallow import Schema, fields
from ..utils.validations import Not_null_string


class QuestionSchema(Schema):
    """ Class to validate schema for Question object """

    user_id = fields.Int(required=True)
    meetup_id = fields.Int(required=True)
    title = fields.Str(required=True, validate= Not_null_string)
    body = fields.Str(required=True, validate= Not_null_string)

    