#!/usr/bin/env python3

# Parent class Fish
class Fish:

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish live in the water")


# Parent class Bird
class Bird:

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird live in the sky")


# FlyingFish class inheriting from both Fish and Bird
class FlyingFish(Fish, Bird):

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# Testing the FlyingFish class
flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()
