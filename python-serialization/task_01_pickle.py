#!/usr/bin/python3
"""
This module defines a CustomObject class to demonstrate
basic serialization and deserialization using Python's pickle module.

Serialization involves saving an object's state to a file,
while deserialization restores the object from that file.
"""
import pickle


class CustomObject:
    """
    A class representing a custom object with attributes such as name,
    age, and student status.

    Attributes:
        name (str): The person's name.
        age (int): The person's age.
        is_student (bool): Whether the person is a student.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes a new instance of CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Indicates if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the details of the CustomObject in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.

        Args:
            filename (str): The name of the file where the object will be saved.
        """
        try:
            with open(filename, 'wb') as pklfile:
                pickle.dump(self, pklfile)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads a serialized CustomObject from a file.

        Args:
            filename (str): The file from which the object will be loaded.

        Returns:
            CustomObject: The deserialized object, or None if deserialization fails.
        """
        try:
            with open(filename, 'rb') as pklfile:
                return pickle.load(pklfile)
        except Exception:
            return None

#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
