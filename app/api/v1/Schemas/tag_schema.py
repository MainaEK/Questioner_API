from marshmallow import Schema, fields
from ..utils.validations import Not_null_string


class TagSchema(Schema):
    """ Class schema to validate tags for Meetup object """

    tags = fields.List(fields.Str,required=True, validate = Not_null_string)