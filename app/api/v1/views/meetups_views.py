from flask import Flask, jsonify, request, Response, json
from ..models.meetups_models import meetups
from ...v1 import v1
from ..utils.validations import sanitize_input


@v1.route('/meetups', methods=['GET'])
def get_all_meetups():
    return jsonify({'status' : 201,'data' : meetups,}),201

