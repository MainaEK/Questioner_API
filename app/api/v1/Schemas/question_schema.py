from marshmallow import Schema, fields
from ..utils.validations import Not_null_string


class QuestionSchema(Schema):
    """ Class to validate schema for Question object """

    q_id = fields.Int(required=True)
    created_on = fields.DateTime(required=True)
    created_by = fields.Int(required=True)
    meetup = fields.Int(required=True)
    title = fields.Str(required=False)
    body = fields.Str(required=True, validate= Not_null_string)
    votes = fields.Int(required=True)
    
    