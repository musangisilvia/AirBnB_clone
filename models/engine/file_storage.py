#!/usr/bin/python3
"""
    Contains the definition of a class FileStorage that serializes instances
    to a JSON file and deserializes JJON files to instances
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Definition of class FileStorage that handles serialization of instances
       to JSON file and deserialization of JSON files to instances
    """

    __file_path = "my_file.json"
    __objects = {}

#    def __init__(self):
#        """Initializes an instance of class FileStorage"""
#        pass

    def all(self):
        """Return the dictionary '__objects'"""
        return self.__objects

    def new(self, obj):
        """Sets a new instance in the '__objects' dictionary using
           <obj class name>.id as the key

        Attributes:
            obj (object): object to be set in the __objects dictionary
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes objects in __objects to the JSON file in __file_path"""
        obj_dicts = {}
        for key, value in self.__objects.items():
            obj_dicts[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='UTF-8') as json_file:
            json.dump(obj_dicts, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects if __file_path exists;
           otherwise does nothing
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='UTF-8') as json_file:
                obj_dicts = json.load(json_file)

            my_objs = {}
            for key, value in obj_dicts.items():
                class_name = value['__class__']
                my_objs[key] = eval(class_name)(**value)
            self.__objects.update(my_objs)
