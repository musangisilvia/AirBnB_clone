#!/usr/bin/python3
"""
    Contains the definition of tests for class City
"""
import unittest
from models.city import City


class TestCityMethods(unittest.TestCase):
    """Definition of tests for class City"""

    def test_attributes_exist(self):
        """Test that class City has the required attributes"""
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))

    def test_City_attributes(self):
        """Test whether the attributes of class City are of the right type"""
        city_1 = City()
        self.assertIsInstance(city_1.name, str)
        self.assertIsInstance(city_1.state_id, str)


if __name__ == '__main__':
    unittest.main()
