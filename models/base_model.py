#!/usr/bin/python3
"""Model of the base parent class all classes inherit from"""
from models import storage
import date
import uuid

class BaseModel:
    """Container of all common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Make an instance of the BaseModel."""
        pass

    def __str__(self):
        """Represent the object in a human readable format."""
        pass

    def to_dict(self):
        """Get a dictionary containing all attributes of instance."""
        pass

    def save(self):
        """Save the attributes at the current time."""
        pass
        # call storage.save()
