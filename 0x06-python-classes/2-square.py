#!/usr/bin/python3
"""
A module of OOp task 3
"""
class Square:
    """
    Creation of a new type Square
    """
    def __init__(self, size=0):
        """
        Initialization of the data size
	"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size=size
