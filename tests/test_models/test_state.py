#!/usr/bin/python3
"""
    Contains the definition of tests for class State
"""
import unittest
from models.state import State


class TestStateMethods(unittest.TestCase):
    """Definition of tests for class State"""

    def test_attributes_exist(self):
        """Test that class User has the required attributes and methods"""
        self.assertTrue(hasattr(State, 'name'))

    def test_State_attributes(self):
        """Test whether the attributes of class State are of the right type"""
        state_1 = State()
        self.assertIsInstance(state_1.name, str)


if __name__ == '__main__':
    unittest.main()
