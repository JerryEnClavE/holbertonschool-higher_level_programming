#!/usr/bin/env python3
from abc import ABC, abstractmethod

# Step 1: Setting up the Abstract Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Step 2: Implementing the Subclasses
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Example usage:
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    
    print(dog.sound())  # Output: Bark
    print(cat.sound())  # Output: Meow
    