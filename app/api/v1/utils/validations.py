from marshmallow import ValidationError
import re

def Not_null_string(value):
    """Validate that string field under validation does not contain null value"""

    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('This parameter cannot be null')
        return value
    elif value:
        return value

def password_check(password):
        if len(password) < 8:
            raise ValidationError("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            raise ValidationError("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            raise ValidationError("Make sure your password has a capital letter in it")
        else:
            return password

