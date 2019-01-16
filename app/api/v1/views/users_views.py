from flask import Flask, jsonify, request, Response, json, abort, make_response
from marshmallow import ValidationError

import datetime
from ..models.user_models import UserModel
from ..Schemas.user_schema import UserSchema
from ...v1 import v1


@v1.route('/auth/signup', methods=['POST'])
def create_user():
    json_data = request.get_json()

    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    data, errors = UserSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))

    elif UserModel().check_exists('username', json_data['username']):
        abort(make_response(jsonify({'status': 400, 'message' : 'Username Already taken'}), 400))

    elif UserModel().check_exists('email', json_data['email']):
        abort(make_response(jsonify({'status': 400, 'message' : 'Email Already exists'}), 400))

    result = UserModel().create_user(json_data)
    

    return jsonify({'status': 201, 'data' : result}), 201
