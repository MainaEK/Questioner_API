from flask import Flask, jsonify, json


def sanitize_input(user_input):
    if('id_' in user_input and 'createdOn' in user_input and 'location' in user_input 
    and 'images' in user_input and 'topic' in user_input and 'happeningOn' in user_input 
    and 'tags' in user_input):
        return True
    else:
        return False  