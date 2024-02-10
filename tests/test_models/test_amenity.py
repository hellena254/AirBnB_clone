#!/usr/bin/python3
"""Tests for the Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
	"""Tests cases as follows"""
	def setUpAmenity(self):
		"""Set up the test environment"""
		self.amenity = Amenity(name="Parking")

	def tearDownAmenity(self):
		"""Tear down the test environment"""
		del self.amenity

	def test_instance(self):
		"""Test creation of instance"""
		self.assertIsInstance(self.amenity, Amenity)
		self.assertIsInstance(self.amenity, BaseModel)

	def test_attributes(self):
		"""Test the attributes"""
		self.assertEqual(self.amenity.name, "Parking")

if __name__ == '__main__':
	unittest.main()
