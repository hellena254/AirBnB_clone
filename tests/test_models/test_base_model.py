#!/usr/bin/python3
"""Test file for the BaseModel class"""
import unittest
import json
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
	"""Test cases as follows"""
	def setUpBasemodel(self):
		"""set up the test env"""
		self.base_model = BaseModel()

	def tearDownBaseModel(self):
		""" Tear down the test env"""
		del self.base_model

	def test_init(self):
		"""Test initialization"""
		self.assertIsInstance(self.base_model, BaseModel)
		self.assertIsInstance(self.base_model.created_at, datetime)
		self.assertIsInstance(self.base_model.updated_at, datetime)

	def test_save(self):
		"""Test the save method of the BaseModel"""
		first_updated_at = self.base_model.updated_at
		self.base_model.save()
		self.assertNotEqual(first-updated_at, self.base_model.updated_at)

	def test_to_dict(self):
		"""Test the to_dict method of the Basemodel"""
		_dict = self.base_model.to_dict()
		self.assertIsInstance(_dict, dict)
		self.assertIn('__class__', _dict)
		self.assertIn('created_at', _dict)
		self.assertIn('updated_at', _dict)

	def test_str(self):
		"""Test the string respresentation of the baseModel class"""
		base_model_str = str(self.base_model)
		self.assertIn('[BaseModel]', base_model_str)
		self.assertIn(str(self.base_model.id), base_model_str)

if __name__ == '__main__':
	unittest.main()




















