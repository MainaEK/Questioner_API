from marshmallow import Schema, fields
from ..utils.validations import Not_null_string


class MeetupSchema(Schema):
    """ Class to validate schema for Meetup object """

    location = fields.Str(required=True, validate= Not_null_string)
    images = fields.List(fields.Str, required=False)
    topic = fields.Str(required=True, validate= Not_null_string)
    happening_on = fields.Date(required=True, validate= Not_null_string)
    tags = fields.List(fields.Str,required=False)