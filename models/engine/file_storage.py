#!/usr/bin/python3
"""Model for handling file storage of the AirBnB project."""
import json

class FileStorage:
    """Serialize/deserialize instances to a JSON file."""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Get a dictionary of all stored objects."""
        pass

    def new(self, obj):
        """Add a new object to the storage (__objects)."""
        pass

    def save(self):
        """Serialize __objects to json."""
        pass

    def reload(self):
        """Deserialize __objects from json."""
        pass
