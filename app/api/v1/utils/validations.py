from flask import Flask, jsonify, json

'''Checks for empty entries in meetups''' 
def sanitize_input(user_input):
    if('id_' in user_input and 'createdOn' in user_input and 'location' in user_input 
    and 'images' in user_input and 'topic' in user_input and 'happeningOn' in user_input 
    and 'tags' in user_input):
        return True
    else:
        return False  

'''Checks for empty entries in questions'''
def sanitize_input_questions(user_input):
    if('id_' in user_input and 'createdOn' in user_input and 'createdBy' in user_input 
    and 'meetup' in user_input and 'title' in user_input and 'body' in user_input 
    and 'votes' in user_input):
        return True
    else:
        return False  