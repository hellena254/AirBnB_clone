#!/usr/bin/python3
"""Tests for the User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
	"""Tests cases as follows"""
	def setUp(self):
		"""Set up the test environment"""
		self.user = User()

	def test_instance(self):
		"""Test if user instance is created successfully"""
		self.assertIsInstance(self.user, User)
		self.assertTrue(hasattr(self.user, 'id'))
		self.assertTrue(hasattr(self.user, 'created_at'))
		self.assertTrue(hasattr(self.user, 'updated_at'))
		self.assertTrue(hasattr(self.user, 'email'))
		self.assertTrue(hasattr(self.user, 'password'))
		self.assertTrue(hasattr(self.user, 'first_name'))
		self.assertTrue(hasattr(self.user, 'last_name'))


if __name__ == '__main__':
	unittest.main()
