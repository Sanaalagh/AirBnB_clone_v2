#!/usr/bin/python3
""" Module for testing DBStorage """
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.base_model import Base


class TestDBStorage(unittest.TestCase):
    """Test the database storage engine."""

    @classmethod
    def setUpClass(cls):
        """Set up for the test suite."""
        cls.storage = DBStorage()

    def test_session_creation(self):
        """Test that a session is created."""
        self.assertIsNotNone(self.storage._DBStorage__session)

    # Add more tests as needed for specific storage methods


if __name__ == '__main__':
    unittest.main()
