#!/usr/bin/python3
"""Module that contains the class BaseGeometry"""


class BaseGeometry:
    """
       A parent class named BaseGeometry
    """
    def area(self):
        """
           Method that raises an exception with message
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
           Method that validates value

           Args:
                param1 (name): string
                param2 (value): value to validate
        """
        self.name = name
        self.value = value

        if type(self.value) is not int:
            raise TypeError('{} must be an integer'.format(self.name))

        if self.value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))


class Rectangle(BaseGeometry):
    """
       A child class Rectangle as a specialization of the parent class
    """
    def __init__(self, width, height):
        """
           __init__ method to initialize the Rectangle
           instance with a width and height

           Args:
                param1 (width): The width of the rectangle
                param2 (height): The height of the rectangle
        """
        if self.integer_validator("width", width):
            self.__width = width

        if self.integer_validator("height", height):
            self.__height = height
