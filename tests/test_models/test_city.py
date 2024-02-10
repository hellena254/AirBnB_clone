#!/usr/bin/python3
"""Tests for the City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
	"""Tests cases as follows"""
	def setUpCity(self):
		"""Set up the test environment"""
		self.city = City(state_id="254", name="Nairobi")

	def tearDownCity(self):
		"""Tear down the test environment"""
		del self.city

	def test_instance(self):
		"""Test creation of instance"""
		self.assertIsInstance(self.city, City)
		self.assertIsInstance(self.city, BaseModel)

	def test_attributes(self):
		"""Test the attributes"""
		self.assertEqual(self.city.name, "Kenya")
		self.assertEqual(self.city.state_id, "254")

if __name__ == '__main__':
	unittest.main()
