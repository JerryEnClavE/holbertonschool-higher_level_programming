#!/usr/bin/env python3
"""Parent class Fish"""


class Fish:
    """Class"""
    def swim(self):
        """Met"""
        print("The fish is swimming")

    def habitat(self):
        """met"""
        print("The fish live in the water")


class Bird:
    """class"""
    def fly(self):
        """met"""
        print("The bird is flying")

    def habitat(self):
        """met"""
        print("The bird live in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class inheriting from both Fish and Bird"""
    def fly(self):
        """met"""
        print("The flying fish is soaring!")

    def swim(self):
        """met"""
        print("The flying fish is swimming")

    def habitat(self):
        """met"""
        print("The flying fish lives both in water and the sky!")
