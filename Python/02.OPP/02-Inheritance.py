# pylint: disable=invalid-name
"""
This file is about inheritance in object-oriented programming (OOP).

Inheritance allows you to create new classes based on existing classes.
The child class inherits all attributes and methods of the parent class,
enabling code reuse and more specialized classes.

In this example, the `Animal` class defines basic animal behavior.
`Dog` and `Cat` inherit from `Animal`, adding their own attributes
and methods while reusing `name` and `walk()`.
"""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def walk(self) -> None:
        print(f"The animal {self.name} is walking")

    def describe(self) -> str:
        return f"Animal: {self.name}"


class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)
        self.breed = breed

    def bark(self) -> None:
        print(f"The dog {self.name} is barking")


class Cat(Animal):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name)
        self.color = color

    def meow(self) -> None:
        print(f"The cat {self.name} is meowing")


# Example usage
dog = Dog("Rex", "Labrador")
print(dog.name)
dog.walk()
dog.bark()

cat = Cat("Whiskers", "Gray")
print(cat.name)
cat.walk()
cat.meow()
