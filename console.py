#!/usr/bin/python3
"""Cmd module."""

import cmd
from models.base_model import BaseModel
import models
import os

class HBNBCommand(cmd.Cmd):
    """The Airbnb Console."""

    prompt = '(hbnb) '

    def emptyline(self):
        """Handles and empty line."""
        pass

    def do_EOF(self, line):
        """Handles end of file."""

        return True

    @staticmethod
    def check_class_name(name):
        """Checks and validates the class name."""
        name = name.split()
        if name == []:
            print("** class name missing **")
        elif name[0] not in globals():
            print("** class doesn't exist **")
        else:
            return globals()[name[0]]

    @staticmethod
    def check_id(line, obj_dict):
        """Checks and validates the object id."""

        name_id = line.split()
        if len(name_id) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(name_id[0], name_id[1])
            if key in obj_dict:
                return True
            else:
                print("** no instance found **")

    @staticmethod
    def get_dict():
        """Retrieves the objects dictionary."""
        models.storage.reload()
        obj_dict = models.storage.all()
        return obj_dict

    @staticmethod
    def get_key(line):
        """Creates a key from the classname and id."""
        name_id = line.split()
        key = "{}.{}".format(name_id[0], name_id[1])
        return key

    @staticmethod
    def get_class(key):
        name_id = key.split('.')
        return name_id[0]

    def do_all(self, line):
        """Prints all the objects regardless of class name."""
        obj_dict = self.get_dict()
        if line:
            name = self.check_class_name(line)
            if name:
                for key, value in obj_dict.items():
                    class_name = self.get_class(key)
                    if class_name == line:
                        print(obj_dict[key])
        else:
            for key, value in obj_dict.items():
                print(obj_dict[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class
        name and id.
        """
        name = self.check_class_name(line)
        if name:
            obj_dict = self.get_dict()
            valid_id = self.check_id(line, obj_dict)
            if valid_id == True:
                key = self.get_key(line)
                del obj_dict[key]
                models.storage.save()

    def do_show(self, line):
        """
        Prints the string representation of the instance
        based on class name and id
        """
        obj_dict = self.get_dict()
        name = self.check_class_name(line)
        if name:
            truth_val = self.check_id(line, obj_dict)
            if truth_val == True:
                key = self.get_key(line)
                print(obj_dict[key])

    def do_create(self, name):
        """
        Creates a new instance of BaseMOdel, saves it
        and prints the id.
        """
        obj_class = self.check_class_name(name)
        if obj_class:
            models.storage.reload()
            obj = obj_class()
            print(obj)
            print(obj.id)
            obj.save()

    def do_quit(self, line):
        """Exits the console."""

        return True

    def do_clear(self, line):
        """Clear the screen."""
        os.system('clear')

if __name__ == '__main__':
    HBNBCommand().cmdloop()

