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
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.__dict__.update(kwargs)
            try:
                del self.__dict__['__class__']
            except Exception:
                pass
            created_str = self.__dict__['created_at']
            updated_str = self.__dict__['updated_at']
            self.__dict__['created_at'] = datetime.strptime(created_str,
                    '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__['updated_at'] = datetime.strptime(updated_str,
                    '%Y-%m-%dT%H:%M:%S.%f')

        key = "{}.{}".format(self.__class__.__name__, self.id)
        obj_dict = models.storage.all()
        if key not in obj_dict:
            models.storage.new(self)


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
        obj_dict = vars(self)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

        
