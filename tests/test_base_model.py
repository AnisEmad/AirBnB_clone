#!/usr/bin/python3
"""
unittest module for BaseModel class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestInstantiation(unittest.TestCase):
    """
    instantiation test
    """
    def test_init(self):
        """Test for init."""
        test = BaseModel()
        self.assertIsInstance(test.id, str)
        self.assertIsInstance(test.created_at, datetime)
        self.assertIsInstance(test.updated_at, datetime)
        del test

    def test_str(self):
        """Test for __str__."""
        test = BaseModel()
        test_str = f"[{test.__class__.__name__}] ({test.id}) {test.__dict__}"
        self.assertEqual(test_str, test.__str__())
        del test

    def test_to_dict(self):
        """Test for to_dict."""
        test = BaseModel()
        test_dict = dict()
        pass
