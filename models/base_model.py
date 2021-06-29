#!/usr/bin/python3
"""
    Contains the definition of the BaseModel class thst defines all common
    attributes and methods for other classes in the AirBnB clone project.
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Definition of the class BaseModel. Defines all common attributes and
       methods for other classes in the AirBnB project
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class.
           Also recreate a class instance from a dictiornary.
        Attributes:
            id (str) - a unique identification number for each class instance
            created_at (datetime) - a datetime object indicating the date
                                    and time the instance was created
            updated_at (datetime) - a datetime object that is updated every
                                    time the instance object is modified
        """
        if kwargs:
            dt = kwargs['updated_at']
            fmt = "%Y-%m-%dT%H:%M:%S.%f"
            self.updated_at = datetime.strptime(dt, fmt)
            dt = kwargs['created_at']
            self.created_at = datetime.strptime(dt, fmt)
            not_use = ["created_at", "__class__", "updated_at"]
            for key, value in kwargs.items():
                if key not in not_use:
                    self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of a class instance in the required
           format
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current
           datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all the relevant key/value pairs of
           an instance, including:
                - all key/value pairs from the __dict__ of the instance
                    - the created_at and updated_at attributes in string format
                      i.e (year-month-day T hour.minute.second.microsecond
                - a key __class__ whose value is the class of the instance
        """
        inst_dict = {key: value for key, value in self.__dict__.items()}
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        inst_dict["__class__"] = self.__class__.__name__
        return inst_dict
