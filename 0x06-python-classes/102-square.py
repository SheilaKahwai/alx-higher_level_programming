#!/usr/bin/python3
"""A class Square that defines a square."""


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiatioon with size.
    Public instance method: def area(self).
    """
    def __init__(self, size=0):
        """Initializes the object's data."""
        self.__size = size

    @property
    def size(self):
        """Retrieves the square's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the square's size to a value."""
        if type(value) is not int or type(value) is not float:
            raise TypeError('size must be a number')
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__self = value

    def area(self):
        """Returns the area of a square."""
        sq_area = self.__size ** 2
        return sq_area
    
