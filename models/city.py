#!/usr/bin/python3
"""
    Contains the definition of class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Definition of class City that inherits from class BaseModel
    Attr:
        state_id (string): the state's id in which the city is located
        name (string): name of the city
    """
    state_id = ""
    name = ""
