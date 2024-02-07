#!/usr/bin/python3
"""A file storage class"""
import json


class FileStorage:
	"""A class that serializes instances to a JSON file 
	and deserializes JSON file to instances.
	Has attributes:
		__file_path: path to the JSON file
		__objects: empty dict but will store all objets
	"""
	__file_path = "my_file.json"
	__objects = {}

	def __init__(self):
		"""Initialize a new instance of the FileStorage class"""

	def all(self):
		"""returns the dictionary __objects"""
		return FileStorage.__objects
	
	def new(self, obj):
		"""sets in __objects the obj with key <obj class name>.id"""
		key = f"{obj.__class__.__name__}.{obj.id}"
		FileStorage.__objects.update({key: obj})

	def save(self):
		"""This method serializes __objects to the JSON file"""
		# declare an empty dcit to hold object
		ser_obj = {}

		# iterate through __objects to obtain key-value pair
		for key, value in FileStorage.__objects.items():
			# convert the values to a dict using to_dict()
			ser_obj[key] = value.to_dict()

			# open the file and store our serialized object into a file using json.dump
			with open(FileStorage.__file_path, "w") as json_file:
				json.dump(ser_obj, json_file)

