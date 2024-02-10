#!/usr/bin/python3
"""Tests for the State class"""
import unittest
from models.state import State
from models import storage


class TestUser(unittest.TestCase):
	"""Tests cases as follows"""
	def setUp(self):
		"""Set up the test environment"""
		self.state = State()

	def test_instance(self):
		"""Test if a State instance is created successfully."""
		self.assertIsInstance(self.state, State)
		self.assertTrue(hasattr(self.state, 'id'))
		self.assertTrue(hasattr(self.state, 'created_at'))
		self.assertTrue(hasattr(self.state, 'updated_at'))
		self.assertTrue(hasattr(self.state, 'name'))

if __name__ == '__main__':
	unittest.main()
