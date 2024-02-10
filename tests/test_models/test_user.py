#!/usr/bin/python3
"""Tests for the User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
	"""Tests cases as follows"""
	def setUpUser(self):
		"""Set up the test environment"""
		self.user = User(email="hellen@example.com", password="pass.123", first_name="Hellen", last_name="Atieno")

	def tearDownUser(self):
		"""Tear down the test environment"""
		del self.user

	def test_instance(self):
		"""Test creation of user instance"""
		self.assertIsInstance(self.user, User)
		self.assertIsInstance(self.user, BaseModel)

	def test_attributes(self):
		"""Test the user attributes"""
		self.assertEqual(self.user.email, "hellen@example.com")
		self.assertEqual(self.user.password, "pass.123")
		self.assertEqual(self.user.first_name, "Hellen")
		self.assertEqual(self.user.last_name, "Atieno")

if __name__ == '__main__':
	unittest.main()
