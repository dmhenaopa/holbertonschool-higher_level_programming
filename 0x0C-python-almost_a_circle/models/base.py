#!/usr/bin/python3
"""Module that contains the class Base"""
import json


class Base:
    """
       A parent class named Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
           Constructor method __init__ to initialize the Base instance

           Args:
                param1 (id): Id of the object
        """
        self.__nb_objects = 0

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """--------------------------METHODS-------------------------"""
    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns the JSON string representation to
            list_dictionaries

            Args:
                 param1 (list_dictionaries): List of dictionaries
        """
        string = "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return string

        string = json.dumps(list_dictionaries)
        return string

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes the JSON string representation of list_objs to a file

            Args:
                 param1 (list_objs): List of instances who inherits of Base
        """
        list_objects = []
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objects = []

        else:
            for object in list_objs:
                list_objects.append(cls.to_dictionary(object))

        with open(filename, mode='w', encoding='utf-8') as my_file:
            my_file.write(cls.to_json_string(list_objects))

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of the JSON string representation
            json_string

            Args:
                 param1 (json_string): string representing list of dictionaries
        """
        list_from_json = []
        if json_string is None or len(json_string) == 0:
            return list_from_json

        else:
            list_from_json = json.loads(json_string)
            return list_from_json
