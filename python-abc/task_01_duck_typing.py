#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """class"""

    @abstractmethod
    def area(self):
        """meat"""
        pass

    @abstractmethod
    def perimeter(self):
        """meat"""
        pass


class Circle(Shape):
    """class"""
    def __init__(self, radius):
        """meat"""
        self.radius = radius

    def area(self):
        """meat"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """meat"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """class"""
    def __init__(self, width, height):
        """meat"""
        self.width = width
        self.height = height

    def area(self):
        """meat"""
        return self.width * self.height

    def perimeter(self):
        """meat"""
        return 2 * (self.width + self.height)

    #
    def shape_info(shape):
        """meat"""
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
