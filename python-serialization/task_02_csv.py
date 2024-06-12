#!/usr/bin/env python3

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON and write it to data.json.
    
    Parameters:
    csv_filename (str): The filename of the input CSV file.
    
    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Read the CSV file
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Convert rows to a list of dictionaries
            data = [row for row in csv_reader]
        
        # Write the JSON file
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True

    except FileNotFoundError:
        print(f"The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Sample test
if __name__ == "__main__":
    csv_file = "data.csv"
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print(f"Failed to convert data from {csv_file}")
