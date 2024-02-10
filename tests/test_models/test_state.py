#!/usr/bin/python3
"""Tests for the State class"""
import unittest
from models.state import State


class TestUser(unittest.TestCase):
	"""Tests cases as follows"""
	def setUpState(self):
		"""Set up the test environment"""
		self.state = State(name="Kenya")

	def tearDownState(self):
		"""Tear down the test environment"""
		del self.state

	def test_instance(self):
		"""Test creation of state instance"""
		self.assertIsInstance(self.state, State)
		self.assertIsInstance(self.state, BaseModel)

	def test_attributes(self):
		"""Test the state attributes"""
		self.assertEqual(self.state.name, "Kenya")

if __name__ == '__main__':
	unittest.main()
