from marshmallow import Schema, fields


class QuestionSchema(Schema):
    """ Class to validate schema for Question object """

    q_id = fields.Int(required=True)
    created_on = fields.DateTime(required=True)
    created_by = fields.Int(required=True)
    m_id = fields.Int(required=True)
    title = fields.Str(required=False)
    body = fields.Str(required=True)
    votes = fields.Int(required=True)
    
    