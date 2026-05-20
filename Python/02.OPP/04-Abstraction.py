# pylint: disable=invalid-name
"""
This file is about abstraction classes and methods.

In Python, abstraction allows you to define a class that can only be
instantiated through a subclass. The user must create a subclass that
overrides or implements the abstract methods.

Use the `abc` module and `ABCMeta` metaclass to enforce that subclasses
implement required methods.
"""

import math
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius
