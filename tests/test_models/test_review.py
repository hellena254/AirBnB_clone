#!/usr/bin/python3
"""Tests for the Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
	"""Tests cases as follows"""
	def setUpReview(self):
		"""Set up the test environment"""
		self.review = Review(place_id="254", user_id = "1", text="satisfied")

	def tearDownReview(self):
		"""Tear down the test environment"""
		del self.review

	def test_instance(self):
		"""Test creation of instance"""
		self.assertIsInstance(self.review, Review)
		self.assertIsInstance(self.review, BaseModel)

	def test_attributes(self):
		"""Test the attributes"""
		self.assertEqual(self.review.text, "satisfied")
		self.assertEqual(self.review.place_id, "254")
		self.assertEqual(self.review.user_id, "1")

if __name__ == '__main__':
	unittest.main()
