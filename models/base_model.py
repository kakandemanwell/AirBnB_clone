#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """base model for the hbnb instance"""
    def __init__(self, *args, **kwargs):
        """Initiates an instance of the basemodel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:

                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """returns a class of attributes"""
        class_name = __class__.__name__
        return ('[{}] ({}) {}'.format(class_name, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values-
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy
        new_dict['__calss__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

