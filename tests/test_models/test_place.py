#!/usr/bin/python3
"""Test Cases for place class"""
import unittest
from models.place import Place
from datetime import datetime

class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up a Place instance for testing."""
        self.place = Place()

    def test_instance_creation(self):
        """Test if a Place instance is created successfully."""
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

if __name__ == '__main__':
	unittest.main()
