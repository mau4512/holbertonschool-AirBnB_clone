#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ Init """
        pass

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict.update({key: value.to_dict()})
        json_file = json.dumps(new_dict)
        with open(FileStorage.__file_path, "w") as my_file:
            my_file.write(json_file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        my_dict = {"BaseModel":BaseModel}
        json_file = ""
        try:
            with open(FileStorage.__file_path, "r") as my_file:
                json_file = json.loads(my_file.read())
                for key in json_file:
                    FileStorage.__objects[key] = my_dict[json_file[key]['__clas\
s__']](**json_file[key])
        except:
            pass
