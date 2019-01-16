# third party imports
from flask import Flask, jsonify, request, Response, json, abort, make_response, current_app
from marshmallow import ValidationError

# standard imports
import jwt
import datetime

# local imports
from ..models.user_models import UserModel
from ..Schemas.user_schema import UserSchema
from ...v1 import v1

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthekey ' 


@v1.route('/auth/signup', methods=['POST'])
def create_user():
    """ Endpoint to create a new user"""
    json_data = request.get_json()
    
    """Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
    
    """Checks if all the required fields have been filled"""
    data, errors = UserSchema().load(json_data)
    if errors:
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400))
    
        """Checks if a similar username exists"""
    elif UserModel().check_exists('username', json_data['username']):
        abort(make_response(jsonify({'status': 400, 'message' : 'Username Already taken'}), 400))
    
        """Checks if a similar email exists"""
    elif UserModel().check_exists('email', json_data['email']):
        abort(make_response(jsonify({'status': 400, 'message' : 'Email Already exists'}), 400))
    
    """Registers the new user and automatically logs them in"""
    result = UserModel().create_user(json_data)
    token = jwt.encode({'username' : json_data['username'], 
      'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 60)}, app.config['SECRET_KEY'])

    return jsonify({'status': 201, 'data' : [{'token' : token.decode('UTF-8'), 'user' : result}]}), 201

@v1.route('/auth/login', methods=['POST'])
def login():
    """ Endpoint to login a user"""
    json_data = request.get_json()
    
    """Checks if there's data and if it's in json format"""
    if not json_data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    """Checks if the user exists"""
    if not UserModel().check_exists("username", json_data['username']):
        abort(make_response(jsonify({'status' : 404,'message' : 'No such user has been registered'}),404))
    
    """Checks if the password is correct"""
    response = UserModel().find('username', json_data['username'])
    if not response['password'] == json_data['password']:
        abort(make_response(jsonify({'status' : 400,'message' : 'Incorrect password'}),400))
    
        """Logs in the user"""
    else:
        token = jwt.encode({'username' : json_data['username'], 
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 60)}, app.config['SECRET_KEY'])
            
        return jsonify({'status': 200, 'data' : [{'token' : token.decode('UTF-8'), 'user' : response}]}), 200

       