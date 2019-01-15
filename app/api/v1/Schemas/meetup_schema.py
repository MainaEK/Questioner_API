from marshmallow import Schema, fields
from ..utils.validations import Not_null_string


class MeetupSchema(Schema):
    """ Class to validate schema for Meetup object """

    m_id = fields.Int(required=True)
    created_on = fields.Date(required=True)
    location = fields.Str(required=True, validate= Not_null_string)
    images = fields.Str(required=False)
    topic = fields.Str(required=True, validate= Not_null_string)
    happening_on = fields.Date(required=True, validate= Not_null_string)
    tags = fields.Str(required=False)