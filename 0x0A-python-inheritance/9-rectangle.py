"""Module 9-rectangle
Contains a class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area():
        """Finds the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Prints an informal string representation of the object."""
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
