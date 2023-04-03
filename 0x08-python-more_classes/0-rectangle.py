#!/usr/bin/python3
"""
Defines a class Rectangle
"""
class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)