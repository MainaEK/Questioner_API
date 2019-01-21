import os
from flask import Flask
from instance.config import app_config
from .database import db_con
from .db_tables import create_db,admin


def create_app(config_name):
    """ Function to initialize Flask app """

    # Initialize app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    
    try:
        connect = db_con()
        create_db(connect)
        admin(connect)
        print("Database successfully connected")    
    except Exception:
        print("Unable to make db connection")
        
    
  
    
    return app

