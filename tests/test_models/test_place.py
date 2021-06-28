#!/usr/bin/python3
"""
    Contains the definition of tests for class Place
"""
import unittest
from models.place import Place


class TestPlaceMethods(unittest.TestCase):
    """Definition of tests for class Place"""

    def test_Place_attributes(self):
        """Test whether the attributes of class Place are of the right type"""
        place_1 = Place()
        self.assertIsInstance(place_1.city_id, str)
        self.assertIsInstance(place_1.user_id, str)
        self.assertIsInstance(place_1.name, str)
        self.assertIsInstance(place_1.description, str)
        self.assertIsInstance(place_1.number_rooms, int)
        self.assertIsInstance(place_1.number_bathrooms, int)
        self.assertIsInstance(place_1.max_guest, int)
        self.assertIsInstance(place_1.price_by_night, int)
        self.assertIsInstance(place_1.latitude, float)
        self.assertIsInstance(place_1.longitude, float)
        self.assertIsInstance(place_1.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
