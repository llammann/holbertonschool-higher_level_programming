#!/usr/bin/python3
"""Module for FlyingFish class"""

class Fish():
    """Fish methods"""
    def swim(self):
        print("The fish is swimming")
    def habitat(self):
        print("The fish lives in water")

class Bird():
    """Bird methods"""
    def fly(self):
        print("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """FlyingFish methods"""
    def fly(self):
        print("The flying fish is soaring!")
    def swim(self):
        print("The flying fish is swimming!")
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
