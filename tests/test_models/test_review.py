#!/usr/bin/python3
"""
    Contains the definition of tests for class Review
"""
import unittest
from models.review import Review


class TestReviewMethods(unittest.TestCase):
    """Definition of tests for class Review"""

    def test_attributes_exist(self):
        """Test that class Review has the required attributes and methods"""
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_Review_attributes(self):
        """Test whether the attributes of class Review are of the right type"""
        review_1 = Review()
        self.assertIsInstance(review_1.place_id, str)
        self.assertIsInstance(review_1.user_id, str)
        self.assertIsInstance(review_1.text, str)


if __name__ == '__main__':
    unittest.main()
