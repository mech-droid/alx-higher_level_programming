#!/usr/bin/python3
"""
Task 2 of the inheritance module
Create qa subclass that sorts a list
"""
class MyList(List):
    """
    Creates a derived class from the base
    class list
    """
    def print_sorted(self):
    """Prints the list in sorted order"""
    n_list = self[]
    n_list.sort()
    print("{}".format(n_list))
