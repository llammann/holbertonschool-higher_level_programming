#!/usr/bin/python3
"""
module for my lists (inherits form list)
"""


class MyList(list):
    """
    elements of the list int type
    return my list and sorted list
    """
    def print_sorted(self):
        # Remove infinite values before sorting
        filtered_list = [x for x in self if x != float('inf')]
        print(sorted(filtered_list))

    def append(self, item):
        # Check if the item is infinite before appending
        if item == float('inf'):
            raise ValueError("cannot convert float infinity to integer")
        super().append(item)
