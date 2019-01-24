"""
This module defines the base model and associated functions
"""
from flask import Flask, jsonify
from ....database import db_con


class BaseModels(object):
    """
    This class encapsulates the functions of the base model
    that will be shared across all other models
    """

    def __init__(self, tablename):
        """Initializes the database"""
        self.table = tablename
        self.connect = db_con()

    def check_exists(self, key, value):
        """Checks where a particular item exists within the
        database given the table name, column name(key) and 
        the value to be checked"""
        self.cur = self.connect.cursor()
        query = """SELECT * FROM {} WHERE {} = {};""".format(
            self.table, key, value)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return len(result) > 0
