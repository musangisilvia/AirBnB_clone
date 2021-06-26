#!/usr/bin/python3
"""
    Contains the definition of the class User that inherits from BaseModel
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a class User that represents a user
    Attributes:
        email (string): email address of user
        password (string): user's password
        first_name (string): user's first name
        last_name (string): user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
