#!/usr/bin/python3
"""Test file for the BaseModel class"""
import unittest
import json
from datetime import datetime
import models.base_model

class TestBaseModel(unittest.TestCase):
	"""Test cases as follows"""
	def setUp(self):
		"""set up the test env"""
		self.base_model = models.base_model.BaseModel()

	def test_init(self):
		"""Test initialization"""
		self.assertIsInstance(self.base_model, models.base_model.BaseModel)
		self.assertIsInstance(self.base_model.created_at, datetime)
		self.assertIsInstance(self.base_model.updated_at, datetime)

	def test_save(self):
		"""Test the save method of the BaseModel"""
		first_updated_at = self.base_model.updated_at
		self.base_model.save()
		self.assertNotEqual(first_updated_at, self.base_model.updated_at)

	def test_to_dict(self):
		"""Test the to_dict method of the Basemodel"""
		base_model_dict = self.base_model.to_dict()
		self.assertIsInstance(base_model_dict, dict)
		self.assertEqual(base_model_dict['__class__'], 'BaseModel')
		self.assertIn('created_at', base_model_dict)
		self.assertIn('updated_at', base_model_dict)

	def test_str(self):
		"""Test the string respresentation of the baseModel class"""
		base_model_str = str(self.base_model)
		self.assertIn('BaseModel', base_model_str)
		self.assertIn(self.base_model.id, base_model_str)

if __name__ == '__main__':
	unittest.main()
