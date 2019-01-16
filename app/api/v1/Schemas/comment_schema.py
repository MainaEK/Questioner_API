from marshmallow import Schema, fields
from ..utils.validations import Not_null_string


class CommentSchema(Schema):
    """ Class to validate schema for Question object """

    q_id = fields.Int(required=True)
    comment = fields.Str(required=True, validate= Not_null_string)