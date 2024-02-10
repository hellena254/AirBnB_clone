#!/usr/bin/python3
"""Tests for the Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
	"""Tests cases as follows"""
	def setUpAmenity(self):
		"""Set up the test environment"""
		self.amenity = Amenity()

	def test_instance(self):
		"""Test creation of instance"""
		self.assertIsInstance(self.amenity, Amenity)
		self.assertTrue(hasattr(self.amenity, 'id'))
		self.assertTrue(hasattr(self.amenity, 'created_at'))
		self.assertTrue(hasattr(self.amenity, 'updated_at'))
		self.assertTrue(hasattr(self.amenity, 'name'))


if __name__ == '__main__':
	unittest.main()
