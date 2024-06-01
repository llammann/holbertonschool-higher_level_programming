#!/usr/bin/python3
"""Module for VerboseList class"""


class VerboseList(list):
    """VerboseList methods"""
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, iterable):
        print(f"Extended the list with [{len(iterable)}] items.")
        super().extend(iterable)

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
