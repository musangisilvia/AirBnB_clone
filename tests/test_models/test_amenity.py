#!/usr/bin/python3
"""
    Contains the definition of tests for class Amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenityMethods(unittest.TestCase):
    """Definition of tests for class Amenity"""

    def test_attributes_exist(self):
        """Test that class Amenity has the required attributes and methods"""
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_Amenity_attributes(self):
        """
           Test whether the attributes of
           class Amenity are of the right type
        """
        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.name, str)


if __name__ == '__main__':
    unittest.main()
