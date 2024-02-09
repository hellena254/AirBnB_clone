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

	def do_show(self, args):
		"""Prints the string representation of an instance based on the class name and id"""
		args = args.split()
		if not args:
			print("** class name missing **")
			return

		if args[0] not in HBNBCommand.class_mapping:
			print("** class doesn't exist **")
		elif len(args) < 2:
			print("** instance id missing **")
		else:
			arguments = "{}.{}".format(args[0], args[1])
			if arguments not in storage.all():
				print("** no instance found **")
			else:
			 	print(storage.all()[arguments])

	def do_destroy(self, args):
		"""Deletes an instance based on the class name and id and save changes into the JSON file"""
		args = args.split()
		if not args:
			print("** class name missing **")
			return

		if args[0] not in HBNBCommand.class_mapping:
			print("** class doesn't exist **")
		elif len(args) < 2:
			print("** instance id missing **")
		else:
			arguments = "{}.{}".format(args[0], args[1])
			if arguments not in storage.all():
				print("** no instance found **")
			else:
			 	del storage.all()[arguments]
			 	storage.save()
			 	storage.reload()

	def do_all(self, args):
		"""Prints all string representation of all instances based or not on the class name"""
		args = args.split()

		if not args:
			list_instance = [str(obj) for obj in storage.all().values()]
			print(list_instance)
		elif args[0] not in HBNBCommand.class_mapping:
			print("** class doesn't exist **")
		else:
			list_instance = [str(obj) for key, obj in storage.all().items() if args[0] == key.split('.')[0]]

			if not list_instance:
				print('[]')
			else:
				print(list_intsance)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
