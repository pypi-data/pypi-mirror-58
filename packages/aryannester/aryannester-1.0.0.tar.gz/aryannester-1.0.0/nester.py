"""This is a distribution which prints each and every elements of a list either using indents or without it. This module
is made by Aryan. Hope you like it. Please comment on PyPI."""


def nester(list_item, level):
    """ This function takes two arguments. One, takes the list whose elements are to be printed and the other, takes
    the amount of indentation required when a nested list occurs.
    """
    for each_item in list_item:
        if isinstance(each_item, list):
            if level == 0:
                nester(each_item, level)
            else:
                nester(each_item, level+1)
        else:
            for tab_stop in range(level):
                print(" \t", end=" ")
            print(each_item)
