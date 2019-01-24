import os
from flask import Flask, jsonify
from flask_jwt_extended import (JWTManager)
from instance.config import app_config
from app.api.v2.views.meetups_views import v2 as meetups_blueprint
from app.api.v2.views.questions_views import v2 as questions_blueprint
from app.api.v2.views.comments_view import v2 as comments_blueprint
from app.api.v2.views.user_views import v2 as users_blueprint
from .database import db_con, db_con_test
from .db_tables import create_db, admin


def create_app(config_name):
    """ Function to initialize Flask app """

    # Initialize app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.url_map.strict_slashes = False
    app.register_blueprint(meetups_blueprint)

    if config_name == 'testing':
        try:
            connect = db_con_test()
            create_db(connect)
            admin(connect)
        except Exception:
            print("Unable to make db_test connection")

    else:
        try:
            connect = db_con()
            create_db(connect)
            admin(connect)
            print("Database successfully connected")
        except Exception:
            print("Unable to make db connection")

    app.config['JWT_SECRET_KEY'] = 'secret'
    jwt = JWTManager(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({
            'status': 404,
            'message': 'Url not found. Check your url and try again'
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'status': 500,
            'message': 'Your request could not be processed'
        }), 500

    return app
