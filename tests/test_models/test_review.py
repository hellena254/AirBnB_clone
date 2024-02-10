#!/usr/bin/python3
"""Tests for the Review class"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
	"""Tests cases as follows"""
	def setUpReview(self):
		"""Set up the test environment"""
		self.review = Review()

	def test_instance(self):
		"""Test creation of instance"""
		self.assertIsInstance(self.review, Review)
		self.assertTrue(hasattr(self.review, 'id'))
		self.assertTrue(hasattr(self.review, 'created_at'))
		self.assertTrue(hasattr(self.review, 'updated_at'))
		self.assertTrue(hasattr(self.review, 'place_id'))
		self.assertTrue(hasattr(self.review, 'user_id'))
		self.assertTrue(hasattr(self.review, 'text'))

if __name__ == '__main__':
	unittest.main()
