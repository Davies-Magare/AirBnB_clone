#!/usr/bin/python3
class dog:

    def __init__(self, **kwargs):
        if not kwargs:
            self.name = 'nada'
            self.age = 'nada'
        else:
            self.__dict__.update(kwargs)

    def validate_info(self):
        print("Name: " + self.name)
        print("Age: " + self.age)
