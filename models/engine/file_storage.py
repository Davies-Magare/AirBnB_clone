#!/usr/bin/python3

"""
Filestorage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        new_dict = {}
        for key, value in self.__objects.items():
            new_value = value.to_dict()
            new_dict[key] = new_value
        with open(self.__file_path, 'w') as file_obj:
            dict_str = json.dumps(new_dict)
            file_obj.write(dict_str)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path) as file_obj:
                dict_str = file_obj.read()
            if dict_str:
                rel_dict = json.loads(dict_str)
                new_dict = {}
                for key, value in rel_dict.items():
                    key_id = key.split('.')
                    if key_id[0] in globals():
                        obj = globals()[key_id[0]](**value)
        except Exception:
            pass
