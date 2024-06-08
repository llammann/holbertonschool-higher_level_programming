#!/usr/bin/python3

import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_list_and_save():
    """
    Adds command-line arguments to a list and saves them to a JSON file.
    """
    if exists("add_item.json"):
        items = load_from_json_file("add_item.json")
    else:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    add_items_to_list_and_save()
