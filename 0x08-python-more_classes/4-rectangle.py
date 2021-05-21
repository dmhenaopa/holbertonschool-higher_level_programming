#!/usr/bin/python3
"""This module contain the Rectangle class and the
   use of attribute as a private attribute
"""


class Rectangle:
    """Class Rectangle that defines a rectangle

       Attributes:
       __width: Private instance attribute
       __height: Private instance attribute
    """
    def __init__(self, width=0, height=0):
        """__init__ method to initialize the Rectangle
           instance with a width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to width of rectange

           Args:
                param1 (value): Width of rectangle object
        """
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')

        elif value < 0:
            raise ValueError('width must be >= 0')

        else:
            self.__width = value

    @property
    def height(self):
        """Getter method to height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to height of rectange

           Args:
                param1 (value): Height of rectangle object        """
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')

        elif value < 0:
            raise ValueError('height must be >= 0')

        else:
            self.__height = value

    def area(self):
        """Calculate the current rectangle area

           Returns:
               int: Area of the rectangle
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Calculate the perimeter of rectangle

           Returns:
               int: Perimeter of the rectangle
        """
        height = self.__height
        width = self.__width
        if height == 0 or width == 0:
            perimeter = 0

        else:
            perimeter = 2 * (height + width)

        return perimeter

    def __str__(self):
        """Print the rectangle with the character #"""
        string = ""
        height = self.__height
        width = self.__width

        if height == 0 or width == 0:
            string = ""

        else:
            for i in range(0, height):
                for j in range(0, width):
                    string += "#"

                if i != height - 1:
                    string += "\n"

                else:
                    continue

        return string

    def __repr__(self):
        """Representational string of the given object"""
        string_width = str(self.__width)
        string_height = str(self.__height)
        string = 'Rectangle(' + string_width + ', ' + string_height + ')'
        return string
