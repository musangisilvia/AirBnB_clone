#!/usr/bin/python3
"""
    Contains the definition of tests for class Place
"""
import unittest
from models.place import Place


class TestPlaceMethods(unittest.TestCase):
    """Definition of tests for class Place"""

    def test_attributes_exist(self):
        """Test that class Place has the required attributes and methods"""
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

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
