#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    __file_path = 'obj_storage.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of objects."""

        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with the key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        #Convert all the objects to dictionaries
        #set them in a new dictionary
        #serialize that dictionary
        new_dict = {}
        for key, value in self.__objects.items():
            new_value = value.to_dict()
            new_dict[key] = new_value
        with open(self.__file_path, 'w') as file_obj:
            dict_str = json.dumps(new_dict)
            file_obj.write(dict_str)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        #Get the string from the file and convert it back to dict
        try:
            with open(self.__file_path) as file_obj:
                dict_str = file_obj.read()
            rel_dict = json.loads(dict_str)
            new_dict = {}
            #Get the key(classname.id as str) and then use it with
            #eval to recreate the object.
            for key, value in rel_dict.items():
                key_id = key.split('.')
                obj = globals()[key_id[0]](**value)
                new_dict[key] = obj
            self.__objects = new_dict
        except Exception:
            pass
