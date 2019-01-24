"""
This contains the schema for posting comments
"""
from marshmallow import Schema, fields
from ..utils.validations import Not_null_string


class CommentSchema(Schema):
    """ Class to validate schema for comment object """

    comment = fields.Str(required=True, validate=Not_null_string)
