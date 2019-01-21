import os
from flask import Flask
from instance.config import app_config
from .database import db_con
from .db_tables import create_db,admin
from app.api.v2.views.meetups_views import v2 as meetups_blueprint
from app.api.v2.views.questions_views import v2 as questions_blueprint
from app.api.v2.views.comments_view import v2 as comments_blueprint


def create_app(config_name):
    """ Function to initialize Flask app """

    # Initialize app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(meetups_blueprint)
    
    try:
        connect = db_con()
        create_db(connect)
        admin(connect)
        print("Database successfully connected")    
    except Exception:
        print("Unable to make db connection")
        
    
  
    
    return app

