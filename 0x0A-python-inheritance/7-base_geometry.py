#!/usr/bin/python3
"""Module that contains the class BaseGeometry"""


class BaseGeometry:
    """
       A class named BaseGeometry
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
