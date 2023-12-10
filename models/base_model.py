#!/usr/bin/python3
import uuid
import models
from datetime import datetime
from datetime import date

"""Basemodel module"""

class BaseModel:
    """Defines all common attributes/methods for other classes."""
    
    def __init__(self, *args, **kwargs):
        """Initializes class attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = self.get_datetime(self.created_at)
            self.updated_at = self.get_datetime(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
        models.storage.new(self)

    @staticmethod
    def get_datetime(str_obj):
        """
        Converts an isoformat string to a datetime object.
        """
        date_obj = datetime.strptime(str_obj, '%Y-%m-%dT%H:%M:%S.%f')
        return date_obj

    def __str__(self):
        """Returns string representation of object."""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, 
                self.__dict__)

    def save(self):
        """Updates updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()        

    def to_dict(self):
        """Returns the dictionary representation of the object."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict

        
