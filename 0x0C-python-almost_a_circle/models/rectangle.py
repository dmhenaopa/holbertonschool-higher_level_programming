#!/usr/bin/python3
"""Module that contains the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
       Class Rectangle that defines a Rectangle instance

       Attributes:
       __width: Private instance attribute
       __height: Private instance attribute
       __x: Private instance attribute
       __y: Private instance attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
           __init__ method to initialize the Rectangle instance
           with width, height and position
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """-------------GETTER AND SETTER METHOD - WIDTH-------------"""
    @property
    def width(self):
        """Getter method to width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to width of Rectangle

           Args:
                param1 (value): width of rectangle object
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        else:
            self.__width = value

    """-------------GETTER AND SETTER METHOD - HEIGHT-------------"""
    @property
    def height(self):
        """Getter method to height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter method to height of Rectangle

           Args:
                param1 (value): height of rectangle object
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')

        else:
            self.__height = value

    """---------------GETTER AND SETTER METHOD - X---------------"""
    @property
    def x(self):
        """Getter method to x position of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setter method to x position of Rectangle

           Args:
                param1 (value): x position of rectangle object
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')

        else:
            self.__x = value

    """---------------GETTER AND SETTER METHOD - Y---------------"""
    @property
    def y(self):
        """Getter method to y position of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setter method to y position of Rectangle

           Args:
                param1 (value): y position of rectangle object
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')

        else:
            self.__y = value

    """--------------------------METHODS-------------------------"""
    def area(self):
        """
           Calculate the current Rectangle area

           Returns:
               int: Area of the rectangle
        """
        area = self.width * self.height
        return area

    def display(self):
        """
           Prints in stdout the Rectangle instance with character
           # by taking care of x and y coordinates
        """
        character = "#"
        height = self.height
        width = self.width
        x = self.x
        y = self.y

        if y > 0:
            for l in range(0, y):
                print('{}'.format(""))

        if height == 0 or width == 0:
            print('{}'.format('""'))

        else:
            for i in range(0, height):
                if x > 0:
                    print('{}'.format(" " * x), end="")

                for j in range(0, width):
                    print('{}'.format(character), end="")

                if i != height - 1:
                    print()

                else:
                    continue
            print()

    def __str__(self):
        """
           Return information about Rectangle instance
        """
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height

        string = ('[Rectangle] ({}) {}/{} - {}/{}'.format(id,
                  x, y, width, height))

        return string

    def update(self, *args, **kwargs):
        """
           Assigns an argument to each attribute

           Args:
                param1 (args): Values of attributes
                param2 (kwargs): Dictionary of arguments
        """
        tuple_len = len(args)
        if args is True or tuple_len != 0:
            if tuple_len >= 1:
                self.id = args[0]

            if tuple_len >= 2:
                self.width = args[1]

            if tuple_len >= 3:
                self.height = args[2]

            if tuple_len >= 4:
                self.x = args[3]

            if tuple_len == 5:
                self.y = args[4]

        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]

                elif key == "width":
                    self.width = kwargs[key]

                elif key == "height":
                    self.height = kwargs[key]

                elif key == "x":
                    self.x = kwargs[key]

                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """
           Returns the dictionary representation of a Rectangle
        """
        id = self.id
        width = self.width
        height = self.height
        x = self.x
        y = self.y

        dictionary = {'x': x,
                      'y': y,
                      'id': id,
                      'height': height,
                      'width': width}

        return dictionary
