#!/usr/bin/python3
"""
Module: task_03_xml

Serialize a Python dictionary to XML and deserialiaze XML
back to a dictionary.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to the filename.

    Args:
        dictionary (dict): The data to serialize.
        filename (str): The output XML filename

    Returns:
        None.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        ET.SubElement(root, key).text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The input XML filename.

    Returns:
        dict: The deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for child in root:
        result[child.tag] = child.text
    return result
