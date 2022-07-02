#!/usr/bin/python3
"""
Task 4 of the module Classes
"""
class Square:
    """
    Creates a new type square
    """
    def __init__(self, size=0):
        """Initializes the data"""
        self.__size = size
    @property
    def size(self):
        """
        A function that returns the size ot square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        A function that modifies the size
        """
        if type(value) != int:
             raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
         """Returns the current square area."""
        return self.__size**2

