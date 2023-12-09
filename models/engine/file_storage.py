#!/usr/bin/python3
"""Model for handling file storage of the AirBnB project."""
import json
import os

class FileStorage:
    """Serialize/deserialize instances to a JSON file."""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Get a dictionary of all stored objects."""
        FileStorage.reload()
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage (__objects)."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to json."""
        for key, value in FileStorage.__objects.items():
            FileStorage.__objects[key] = value.to_dict()
            #del FileStorage.__objects[key]["__class__"]
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)
        

    def reload(self):
        """Deserialize __objects from json."""
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
        for key, value in FileStorage.__objects.items():
            FileStorage.__objects[key] = BaseModel(**value)
