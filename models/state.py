#!/usr/bin/python3
"""
    Contains the definition of class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Definition of class State that inherits from BaseModel
    Attr:
        name (string): name of the state where a Place is located
    """
    name = ""
