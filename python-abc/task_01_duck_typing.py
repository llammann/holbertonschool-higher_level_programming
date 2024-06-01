#!/usr/bin/python3
"""module for Duck typing Shape class"""


from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    """Shape class abstract methods"""
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Circle class methods"""
    def __init__(self, radius):
        self.radius = abs(radius)
    def area(self):
        return pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    """Rectangle class methods"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2 * (self.height + self.width)
    
def shape_info(Shape):
    """ accept an object of type shape and prints its area and perimeter"""
    print("Area:", Shape.area())
    print("Perimeter:", Shape.perimeter())
