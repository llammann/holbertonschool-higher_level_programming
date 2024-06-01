#!/usr/bin/python3
"""Module with two mixin classes and Dragon class"""


class SwimMixin:
    """Swimmixing methods"""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """FlyMixin methods"""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon methods"""
    def roar(self):
        print("The dragon roars!")
