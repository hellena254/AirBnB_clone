#!/usr/bin/python3
"""The BaseModel Class"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:

	"""class constructor"""
	def __init__(self, *args, **kwargs):
		"""define the attributes:
			id, created_at, updated_at
		"""

		if kwargs:
			"""if kwargs is not empty"""
			del kwargs["__class__"]
			for key, value in kwargs.items():
				"""convert created_at and updated_at from strings to datetime objects"""
				if key == "created_at" or key == "updated_at":
					datetime_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
					setattr(self, key, datetime_obj)
				else:
					setattr(self, key, value)
		else:
			"""if its empty"""
			self.id = str(uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)

	def save(self):
		"""update the updated_time with the current dat e and time"""
		updated_at = datetime.now()
		models.storage.save()
	
	def to_dict(self):
		"""returns a dictionary containing all key/value of __dict__
		empty dictionary that will hold or return the dictionary representation of our class instance attributes after the serialization"""
		class_dict = {}		
		# add a class key to identify the class name
		class_dict["__class__"] = self.__class__.__name__

		for key, value in self.__dict__.items():
			# get values which are of type datetime
			if isinstance(value, datetime):
				# convert them to ISO format
				class_dict[key] = value.isoformat()
			else:
				class_dict[key] = value
		return class_dict

	def __str__(self):
		"""string representation of the objects"""
		return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"


# tests
my_model = BaseModel()
my_model.name = "hellen"
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

