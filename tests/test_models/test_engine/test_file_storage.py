#!/usr/bin/python3
"""Test file for the FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import os
import json
import unittest

class TestFileStorage(unittest.TestCase):
	"""The test cases are as follows"""
	def setUpFilestorage(self):
		"""Set up the test environment"""
		self.file_storage = FileStorage()
		self.base_model = BaseModel()

	def tearDownStorage(self):
		"""Tear down the file storage test env"""
		del self.file_storage
		del self.base_model

	def test_init(self):
		"""Test Initialization"""
		self.assertIsInstance(self.file_storage, FileStorage)

	def test_all(self):
		"""Test the all method"""
		all_obj = self.file_storage.all()
		self.assertIsInstance(all_obj, dict)
		self.assertIn('BaseModel.' + self.base_model.id, all_obj)

	def test_new(self):
		"""test the new method"""
		key = 'BaseModel.' + self.base_model.id
		self.assertNotIn(key, self.file_storage.all())
		self.file_storage.new(self.base_model)
		self.assertIn(key, self.file_storage.all())

	def test_save_reload(self):
		"""Test save and reload methos"""
		key = 'BaseModel.' + self.base_model.id
		self.file_storage.new(self.base_model)
		self.file_storage.save()
		self.file_storage.reload()
		all_objects = self.file_storage.all()
		self.assertIsInstance(all_objects, dict)
		self.assertIn(key, all_objects)

if __name__ == '__main__':
	unittest.main()
