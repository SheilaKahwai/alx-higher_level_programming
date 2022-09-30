#!/usr/bin/python3
"""Module Rectangle
Contains the class Rectangle that inherits from Base
"""


class Rectangle(Base):
    """Represents a Rectangle.
    Private instance attribute: width
        - property def width(self)
        - property setter def width(self, value)
    Private instance attribute: height
        - property def height(self)
        - property setter def height(self, value)
    Private instance attribute: x
        - property def x(self)
        - property setter def x(self, value)
    Private instance attribute: y
        - property def y(self)
        - property setter def y(self, value)
    Class constructor: def __init__(self, width, height, x=0, y=0, id=None)
    Public instance method: def area(self)
    Public instance method: def display(self)
    Public instance method: def update(self, *args)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises our Rectangle instance."""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to the value"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to the value."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

    @property
    def x(self):
        """Retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x to value."""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

    @property
    def y(self):
        """Retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y to value."""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

    def area(self):
        """Calculates the area of our rectangle instance
        Returns:
            - the area value.
        """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in self.__height:
            print(' ' * self.__y)
            for j in self.__width:
                print(' ' * self.__x)
                print('#', end="")
            print()

    def __str__(self):
        """Prints an informal string representation of an object."""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__name__, self.__id, self.__x,\
                self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.
        Args:
            - *args: positional arguments
            - **kwargs: keyworded arguments
        """
        self.__id = args[0]
        self.__width = args[1]
        self.__height  = args[2]
        self.__x = args[3]
        self.__y = args[4]
