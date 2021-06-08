#!/usr/bin/python3
"""Module that contains the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
       Class Square that defines a Square instance

       Attributes:
       __width: Private instance attribute
       __height: Private instance attribute
       __x: Private instance attribute
       __y: Private instance attribute
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            __init__ method to initialize the Square instance
            with size, position and id
        """
        super().__init__(size, size, x, y, id)

    """-------------GETTER AND SETTER METHOD - SIZE-------------"""
    @property
    def size(self):
        """Getter method to width of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method to size of Square

           Args:
                param1 (value): width of square object
        """
        self.width = value
        self.height = value

    """--------------------------METHODS-------------------------"""

    def __str__(self):
        """
           Return information about Square instance
        """
        id = self.id
        x = self.x
        y = self.y
        size = self.width

        string = ('[Square] ({}) {}/{} - {}'.format(id, x, y, size))

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
                self.size = args[1]

            if tuple_len >= 3:
                self.x = args[2]

            if tuple_len >= 4:
                self.y = args[3]

        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]

                elif key == "size":
                    self.size = kwargs[key]

                elif key == "x":
                    self.x = kwargs[key]

                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """
           Returns the dictionary representation of a Square
        """
        id = self.id
        size = self.size
        x = self.x
        y = self.y

        dictionary = {'id': id,
                      'x': x,
                      'size': size,
                      'y': y}

        return dictionary
