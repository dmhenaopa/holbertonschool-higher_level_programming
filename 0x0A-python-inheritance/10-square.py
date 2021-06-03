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
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
           Area method override from class BaseGeometry
           Method to calculate the area of the rectangle
        """
        area_rectangle = self.__width * self.__height
        return area_rectangle

    def __str__(self):
        """
           Method str to return a printable format of info
           about the rectangle
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
       A child class Square that inherits from Rectangle class
    """
    def __init__(self, size):
        """
           _init__ method to initialize the Square
           instance with the size

           Args:
                param1 (size): The size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
           Area method override from class BaseGeometry and Rectangle
           Method to calculate the area of the square
        """
        area_square = self.__size * self.__size
        return area_square
