#!/usr/bin/python3
"""
    Contains the definition of the class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Definition of class Place that inherits from class BaseModel
    Attr:
        city_id (string): ID of the city the place is in
        user_id (string): ID of the person who's put up the place on AirBnb
        name (string): name of the place
        description (string): Description of the place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests the place can host
        price_by_night (int): price to hire the place per night
        latitude (float): latitude coordinate of the place
        longitude (float): longitude coordinate of the place
        amenity_ids (list): a list of amenities (Amenity.id)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
