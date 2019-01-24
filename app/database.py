"""
This module is for making the database connection
"""
import os
import psycopg2

from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_TEST_URL = os.environ.get('DATABASE_TEST_URL')


def db_con():
    """Making the connection to the database"""
    try:
        con = psycopg2.connect(DATABASE_URL)

    except Exception:
        print("Unable to make database connection")

    return con


def db_con_test():
    """Making the connection to the test database"""
    try:
        con = psycopg2.connect(DATABASE_TEST_URL)

    except Exception:
        print("Unable to make database connection")

    return con
