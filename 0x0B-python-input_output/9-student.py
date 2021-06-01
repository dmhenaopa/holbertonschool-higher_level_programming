#!/usr/bin/python3
"""Module has a class Student"""


class Student:
    """
       Class Student that defines a Student

       Attributes:
       first_name, last_name and age
    """
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """
           __init__ method to initialize the Student
           instance with first, last name and age

           Args:
                param1 (first_name): The first name of student
                param2 (last_name): The last name of student
                param3 (age): The age of student
         """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
           Function that retrieves a dictionary representation of a
           Student instance
        """
        variables = vars(self)
        return variables
