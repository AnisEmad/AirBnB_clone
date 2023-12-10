#!/usr/bin/python3
"""
unittest module for FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestInstantiation(unittest.TestCase):
    """
    instantiation test
    """
    def test_init(self):
        """test"""
        pass

class TestFileStorage(unittest.TestCase):

    def test_all_empty(self):
        pass
    
    def test_new(self):
        test_storage = FileStorage()
        test_base = BaseModel()
        test_key = f"{test_base.__class__.__name__}.{test_base.id}"
        test_storage.new(test_base)
        for key in FileStorage._FileStorage__objects:
            if (key == test_key):
                self.assertEqual(key, test_key)
        self.assertEqual(test_base,FileStorage._FileStorage__objects[test_key])

    def test_save(self):
        pass


if __name__ == '__main__':
    unittest.main()
