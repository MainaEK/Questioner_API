from marshmallow import Schema, fields
from ..utils.validations import Not_null_string


class ImageSchema(Schema):
    """ Class schema to validate images for Meetup object """

    images = fields.List(fields.Str,required=True, validate = Not_null_string)