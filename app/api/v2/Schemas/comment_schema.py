from marshmallow import Schema, fields
from ..utils.validations import Not_null_string


class CommentSchema(Schema):
    """ Class to validate schema for Question object """

    question_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    body = fields.Str(required=True, validate= Not_null_string)