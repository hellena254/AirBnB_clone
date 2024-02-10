#!/usr/bin/python3
"""Tests for the City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
	"""Tests cases as follows"""
	def setUpCity(self):
		"""Set up the test environment"""
		self.city = City()

	def test_instance(self):
		"""Test creation of instance"""
		self.assertIsInstance(self.city, City)
		self.assertTrue(hasattr(self.city, 'created_at'))
		self.assertTrue(hasattr(self.city, 'updated_at'))
		self.assertTrue(hasattr(self.city, 'state_id'))
		self.assertTrue(hasattr(self.city, 'name'))


if __name__ == '__main__':
	unittest.main()
