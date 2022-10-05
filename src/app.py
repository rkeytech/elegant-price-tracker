"""This is the main file for running the application"""
import os
import string


def add_element(element) -> [string]:
    """
    Adds a new string element in a list and returns it
    :rtype: List of string elements
    """
    temp_list = [element]
    return temp_list


if __name__ == "__main__":
    test = os.path.dirname(__file__)
    mylist = add_element("my list")
    print(mylist)
