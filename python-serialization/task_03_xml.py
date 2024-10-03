#!/usr/bin/python3
"""
XML Serialization and Deserialization Module.

This module provides functionality to serialize a Python dictionary
into an XML file and deserialize an XML file back into a Python dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML data.
    """
    """Create the root element <data>."""
    root = ET.Element("data")

    """Iterate through the dictionary items and
    add them as child elements."""
    for key, value in dictionary.items():
        """Create a child element for each key-value pair."""
        child = ET.SubElement(root, key)
        """Ensure the value is a string."""
        child.text = str(value)

    """Create an ElementTree object and write to the file."""
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file back into a Python dictionary.

    Args:
        filename (str): The name of the file to read the XML data from.

    Returns:
        dict: A dictionary containing the deserialized data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ET.ParseError: If the XML file is not well-formed.
    """
    """Parse the XML file and get the root element."""
    tree = ET.parse(filename)
    root = tree.getroot()

    """Create a dictionary to hold the deserialized data."""
    deserialized_dict = {}
    for child in root:
        deserialized_dict[child.tag] = child.text

    return deserialized_dict
