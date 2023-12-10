#!/usr/bin/python3
"""module for manging reviews."""
from models.base_model import BaseModel


class Review(BaseModel):
   """Create new review."""
    place_id = ""
    user_id = ""
    text = ""
