#!/usr/bin/env python3

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes the given dictionary to a JSON file.
    
    Parameters:
    data (dict): A Python Dictionary with data
    filename (str): The filename of the output JSON file. If the output file already exists it should be replaced.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Loads and deserializes the data from the specified JSON file.
    
    Parameters:
    filename (str): The filename of the input JSON file
    
    Returns:
    dict: A Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data
