# third party imports
from flask import Flask, jsonify, request, Response, json, abort, make_response, current_app
from marshmallow import ValidationError
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)

# standard imports
import datetime

# local imports
from ..models.user_models import UserModel
from ..Schemas.user_schema import UserSchema
from ...v2 import v2
 

@v2.route('/auth/signup', methods=['POST'])
def create_user():
    """ Endpoint to create a new user"""
    json_data = request.get_json()
    print(json_data)
    
    """Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
    
    """Checks if all the required fields have been filled"""
    data, errors = UserSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))
    
        """Checks if a similar username exists"""
    elif UserModel().check_exist('username', json_data['username']):
        abort(make_response(jsonify({'status': 400, 'message' : 'Username Already taken'}), 400))
    
        """Checks if a similar email exists"""
    elif UserModel().check_exist('email', json_data['email']):
        abort(make_response(jsonify({'status': 400, 'message' : 'Email Already exists'}), 400))
    
    """Registers the new user and automatically logs them in"""
    result = UserModel().create_user(json_data)
    
    return jsonify({'status': 201, 'data' : [{'user' : result}]}), 201