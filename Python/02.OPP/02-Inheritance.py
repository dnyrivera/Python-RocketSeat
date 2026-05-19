"""
This file is about inheritance in object-oriented programming (OOP).

Inheritance is a fundamental concept in object-oriented programming that allows you to create new classes based on existing classes. The new class, called the "child" class, inherits all the attributes and methods of the existing class, called the "parent" class. This allows you to reuse code and create more specialized classes.

In this example, we have an `Animal` class that defines the basic behavior of an animal. The `Animal` class has a `name` attribute and a `walk()` method.

We then create two child classes, `Dog` and `Cat`, that inherit from the `Animal` class. The `Dog` and `Cat` classes have their own attributes and methods, but they also inherit the `name` attribute and `walk()` method from the `Animal` class.

This allows us to create instances of the `Dog` and `Cat` classes that can walk like animals, but also have their own unique behavior.

"""

class Animal():
    def __init__(self, name: str) -> None:
        self.name = name

    def walk(self) -> None:
        print(f"The animal {self.name} is walking")
        return

class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)
        self.breed = breed

    def bark(self) -> None:
        print(f"The dog {self.name} is barking")
        return

class Cat(Animal):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name)
        self.color = color

    def meow(self) -> None:
        print(f"The cat {self.name} is meowing")
        return

# Example usage
dog = Dog("Rex", "Labrador")
print(dog.name)
dog.walk()
dog.bark()

cat = Cat("Whiskers", "Gray")
print(cat.name)
cat.walk()
cat.meow()