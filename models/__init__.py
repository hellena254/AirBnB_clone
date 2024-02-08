#!/usr/bin/python3
"""Initialization for the models package"""


# import file_storage.py to create an instance of FileStorage
from models.engine.file_storage import FileStorage

# create a variable storage
storage = FileStorage()

# call reload()
storage.reload()
