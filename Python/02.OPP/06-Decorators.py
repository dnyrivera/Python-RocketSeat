# pylint: disable=invalid-name
"""
This file is about decorators in Python.

A decorator takes another function as an argument and returns a modified
version of that function, allowing you to change behavior without modifying
the source code directly.

Covers: basic decorators, class-based decorators, @classmethod,
@staticmethod, and @property.
"""

# Basic decorator
# A decorator takes another function as an argument and returns a modified version.

# Define a decorator function that adds some behavior before and after the function


def my_decorator(func):
    def wrapper():
        # Do something before the function runs
        print("Something is happening before the function runs")

        # Call the decorated function
        func()

        # Do something after the function runs
        print("Something is happening after the function runs")

    # Return the modified function
    return wrapper


# Apply the decorator to the `say_hello` function


@my_decorator
def say_hello():
    print("Hello!")


# Call the decorated function
say_hello()

# Decorator Commons
# `@classmethod` - Allows a method to be called on the class itself, not on an instance.
# `@staticmethod` - Allows a method to be called on the class without instance data.
# `@property` - Defines a method as a getter for a class attribute.

# Here's an example of using a class as a decorator:


class MyClassDecorator:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> None:
        print("Something is happening before the function runs")
        self.func()
        print("Something is happening after the function runs")

    def describe(self) -> str:
        return f"Decorator wrapping: {self.func.__name__}"


@MyClassDecorator
def say_hello_on_class():
    print("Calling MyClass Decorator Function!")


say_hello_on_class()


# Here's an example of `@classmethod` and `@staticmethod`:


class MyClass:

    value = 10

    def __init__(self, name) -> None:
        self.name = name  # Instance attribute

    def method_instance(self):  # Need a instance to be called
        return f"Instance Method: {self.name}"

    @classmethod
    def method_class(cls):  # Can be called without instance using the class (cls)
        return f"Class Method: {cls.value}"

    @staticmethod
    def method_static():  # Can be called without instance
        return "Static Method"


# Usage
obj = MyClass("Example Class")

print(obj.method_instance())  # Need a instance to be called
print(obj.method_class())  # Can be called without instance
print(obj.method_static())  # Can be called without instance
print(obj.value)  # Can be called without instance


# Here's an example of using `@classmethod` as a factory method:


class Car:
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"

    @classmethod
    def create_car(cls, setup):
        brand, model, year = setup.split(",")
        return cls(brand, model, int(year))


SETUP_TOYOTA = "Toyota, Corolla,2022"
car_01 = Car.create_car(setup=SETUP_TOYOTA)
print(f"Marca:{car_01.brand}\nModelo:{car_01.model}\nAno:{car_01.year}")


class Mathematic:
    @staticmethod
    def sum_numbers(x: int, y: int) -> int:
        return x + y

    @staticmethod
    def multiply_numbers(x: int, y: int) -> int:
        return x * y


print(Mathematic.sum_numbers(x=10, y=15))
