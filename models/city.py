#!/usr/bin/python3
"""Module for manging cities."""

from models.base_model import BaseModel

class City(BaseModel):
    """Create new city."""
    name = ""
    state_id = ""
