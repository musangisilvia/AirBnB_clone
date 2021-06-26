#!/usr/bin/python3
"""
    contains the definition class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Definition of class Amenity that inherits from class BaseModel
    Attr:
        name (string): name of the amenities available at the Place
    """
    name = ""
