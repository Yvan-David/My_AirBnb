#!/usr/bin/python3
""" a module that have a base model of the project """
import uuid
from datetime import datetime

class BaseModel:
    """ a class that creates base model of every instance """
    def __init__(self):
        """ initiates base attributes """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ method that returns str reprentation of the class """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ method that updates updated_at """
        self.updated_at = datetime.today()

    def to_dict(self):
        """ customised dictionary """
        to_dict = {}
        to_dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            to_dict[key] = value
            if key == 'created_at' or key == 'updated_at':
                to_dict[key] = datetime.isoformat(value)
        return to_dict

