#!/usr/bin/python3
"""Module base
Includes the projects base class Base.
"""


class Base:
    """base class of our project.
    Public instance attribute: id
    Private class attribute: __nb_objects = 0
    Class constructor: def __init__(self, id=None)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes our class instance.
        Args:
            - id: argument value of type int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
