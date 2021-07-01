#!/usr/bin/python3
"""
    Contains tests for the user class.
"""
import unittest
from models.user import User


class TestUserMethods(unittest.TestCase):
    """Defines the tests to be carried out on User's class methods"""

    def test_attributes_exist(self):
        """Test that the class User has the required attributes"""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_attribute_types(self):
        """Test whether the class attributes are of the right type"""
        user_1 = User()
        self.assertIsInstance(user_1.email, str)
        self.assertIsInstance(user_1.password, str)
        self.assertIsInstance(user_1.first_name, str)
        self.assertIsInstance(user_1.last_name, str)


if __name__ == '__main__':
    unittest.main()
