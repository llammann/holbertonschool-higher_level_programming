#!/usr/bin/python3
""" Define abstract class Animal """

from abc import ABC, abstractmethod
class Animal(ABC):
    """Animal class methods"""
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
      """Dog class methods"""
      def sound(self):
            return "Bark"
class Cat(Animal):
      """Cat class methods"""
      def sound(self):
            return "Meow"
