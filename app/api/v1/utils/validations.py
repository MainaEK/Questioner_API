from marshmallow import ValidationError

def Not_null_string(value):
    """Validate that string field under validation does not contain null value"""

    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('This parameter cannot be null')
        return value
    elif value:
        return value

