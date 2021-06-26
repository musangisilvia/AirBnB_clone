#!/usr/bin/python3
"""
    contains the definition of class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Definition of class Review that inherits from class BaseModel
    Attr:
        place_id (string): Place.id of the place that's been reviewed
        user_id (string): User.id of the user that wrote the review
        text (string): review of the place
    """
    place_id = ""
    user_id = ""
    text = ""
