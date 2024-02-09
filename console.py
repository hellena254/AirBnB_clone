#!/usr/bin/python3
"""
 contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
	"""
	A prompt(hbnb)
	A dictionary to map class name to objects
	"""
	prompt = '(hbnb) '
	#class_mapping = {'BaseModel': BaseModel}
	class_mapping = ["BaseModel"]

	def do_quit(self, args):
		"""Quit command to exit the program

		"""
		return True

	def do_EOF(self, args):
		"""EOF command to exit program

		"""
		print()
		return True
	
	def emptyline(self):
        	"""Do nothing on empty input line"""
        	pass

	def do_create(self, args):
		"""Create a new instance of the BaseModel"""
		if not args:
			print("** class name missing **")
			return

		if args not in HBNBCommand.class_mapping:
			print("** class doesn't exist **")
		else:
			created = eval(args)()
			print(created.id)
			created.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
