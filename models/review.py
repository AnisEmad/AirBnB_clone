#!/usr/bin/python3
""" module for manging reviews """

from base_model import BaseModel

class City(BaseModel):
    """ Create new review """
    place_id = ""
    user_id = ""
    text = ""
