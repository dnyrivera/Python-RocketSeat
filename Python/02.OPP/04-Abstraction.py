"""
This file is about abstraction classes and methods.

In Python, abstraction allows you to define a class that can only be instantiated through a subclass. This means that you can create a class with certain methods or attributes that are not meant to be accessed or modified directly by the user. Instead, the user must create a subclass that overrides or implements these methods or attributes.

To create an abstract class in Python, you can use the `abc` module. The `abc` module provides a `ABCMeta` class that you can use as a metaclass for your abstract class. This metaclass ensures that any class that inherits from the abstract class must implement certain methods.

Here's an example of an abstract class in Python:

"""
from abc import ABCMeta, abstractmethod
import math


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
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius
