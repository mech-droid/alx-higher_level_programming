#!/usr/bin/python3
"""
Task 3 of the Square project
"""
class Square:
    """
    A empty creation of square
    """
    def __init__(self, size=0):
        """
        Initialization of the size data
        """
        if type(size) != int :
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size=size
    def area(self):
        """A function that returns the area of a square"""
        return self.__size * self.__size
