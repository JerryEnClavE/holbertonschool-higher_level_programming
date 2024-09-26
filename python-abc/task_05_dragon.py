#!/usr/bin/env python3


class SwimMixin:
    """class"""
    def swim(self):
        """meat"""
        print("The creature swims!")


class FlyMixin:
    """class"""
    def fly(self):
        """meat"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """class"""
    def roar(self):
        """meat"""
        print("The dragon roars!")
