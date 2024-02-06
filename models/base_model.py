from datetime import datetime
from uuid import uuid4

class BaseModel:

	"""class constructor"""
	def __init__(self):
		"""define the attrributes:
			id, created_at, updated_at
		"""
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def save(self):
		"""update the updated_time with the current dat e and time"""
		updated_at = datetime.now()
	
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
		return f"{self.__class__.__name__} {self.id} {self.__dict__}"


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
