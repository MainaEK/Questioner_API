from marshmallow import Schema, fields, post_dump
from ..utils.validations import required


class MeetupSchema(Schema):
    '''Class to validate schema for Meetup object'''

    m_id = fields.Int(dump_only=True)
    created_on = fields.Str(dump_only=True)
    location = fields.Str(required=True, validate=(required))
    images = fields.List(fields.Str(), required=False)
    topic = fields.Str(required=True, validate=(required))
    happening_on = fields.Str(required=True, validate=(required))
    tags = fields.List(fields.Str(), required=False)
    