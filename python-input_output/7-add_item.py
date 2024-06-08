#!/usr/bin/python3
"""
This module contains a function `add_items_to_list_and_save`.
"""

import sys
from os.path import exists

import 5-save_to_json_file
import 6-load_from_json_file


def add_items_to_list_and_save():
    """
    Adds command-line arguments to a list and saves them to a JSON file.
    """
    if exists("add_item.json"):
        items = 6-load_from_json_file.load_from_json_file("add_item.json")
    else:
        items = []

    items.extend(sys.argv[1:])

    5-save_to_json_file.save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    add_items_to_list_and_sav)
