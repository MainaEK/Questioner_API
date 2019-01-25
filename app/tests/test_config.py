"""
This module contains the tests for the configurations
"""
# standard imports
import unittest
from app import create_app


class TestDevelopmentConfig(unittest.TestCase):
    """ Test class for development config """

    def setUp(self):
        """Initialize app"""
        self.app = create_app('development')

    def test_app_is_development(self):
        """ Test function for development environment """
        self.assertEqual(self.app.config['DEBUG'], True)
        self.assertEqual(self.app.config['TESTING'], False)

    def tearDown(self):
        """Clear app"""
        self.app = None


class TestTestingConfig(unittest.TestCase):
    """ Test class for testing config """

    def setUp(self):
        """Initialize app"""
        self.app = create_app('testing')

    def test_app_is_development(self):
        """ Test function for testing environment """
        self.assertEqual(self.app.config['DEBUG'], False)
        self.assertEqual(self.app.config['TESTING'], True)

    def tearDown(self):
        """Clear app"""
        self.app = None
