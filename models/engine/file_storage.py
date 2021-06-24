#!/usr/bin/python3
"""
    Contains the definition of a class FileStorage that serializes instances
    to a JSON file and deserializes JJON files to instances
"""
import json
import os.path


class FileStorage():
    """Definirion of class FileStorage that handles serialization of instances
       to JSON file and deserialization of JSON files to instances
    """

    __file_path = "my_file.json"
    __objects = {}

    def __init__(self):
        """Initializes an instance of class FileStorage"""
        pass

    def all(self):
        """Return the dictionary '__objects'"""
        return __objects

    def new(self, obj):
        """Sets a new instance in the '__objects' dictionary using
           <obj class name>.id as the key

        Attributes:
            obj (object): object to be set in the __objects dictionary
        """
        key = obj.__name__.class + obj.id
        __objects[key] = obj

    def save(self):
        """Serializes objects in __objects to the JSON file in __file_path"""
        obj_dicts = {}
        for key, value in __objects.items():
            obj_dicts[key] = value.to_dict()
        with open(__file_path, mode='w', encoding='UTF-8') as json_file:
            json.dump(obj_dicts, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects if __file_path exists;
           otherwise does nothing
        """
        if os.path.isfile(__file_path):
            with open(__file_path, mode='r', encoding='UTF-8') as json_file:
                obj_dicts = json.load(json_file)

            my_objs = {}
            for key, value in obj_dicts:
                if value['__class__'] == 'BaseModel':
                    my_objs[key] = BaseModel(**value)

            __objects.update(my_objs)
