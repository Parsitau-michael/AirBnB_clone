#!/usr/bin/env python3
"""
This module represents the BaseModel class
"""


import uuid
from datetime import datetime


class BaseModel():
    """
    This class defines all common attributes/methods for other classes.
    """

    def __init__(self):
        """
        Initializes an instance of BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Improved __str__ to format the dictionary properly.
        """
        return '[{}] ({}) {}'.format(
                                    self.__class__.__name__,
                                    self.id,
                                    self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' timestamp to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Includes all instance attributes and converts datetime objects
        to ISO format for serialization.
        """
        return {
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat(),
                '__class__': self.__class__.__name__,
                **self.__dict__
                }
