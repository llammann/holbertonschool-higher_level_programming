#!/usr/bin/env python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to the given filename.
    
    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The filename to save the XML data to.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.
    
    Parameters:
    filename (str): The filename to read the XML data from.
    
    Returns:
    dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    
    return dictionary

# Sample test
if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
