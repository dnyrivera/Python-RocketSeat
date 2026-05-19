"""
This file is about decorators in Python.

A decorator is a function that takes another function as an argument and returns a modified version of that function. Decorators are a powerful tool in Python that allow you to modify the behavior of functions and methods without modifying their source code.

In this example, we define a basic decorator function that adds some behavior before and after the decorated function is called. We then apply the decorator to the `say_hello` function and call the decorated function.

We also provide an overview of other commonly used decorators in Python, such as `@classmethod`, `@staticmethod`, and `@property`. These decorators are not used in the code in this file, but they are commonly used in Python to modify the behavior of methods and attributes in classes.

"""

# Basic decorator
# A decorator is a function that takes another function as an argument and returns a modified version of that function.

# Define a decorator function that adds some behavior before and after the decorated function is called
from typing import Any


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
    # Call the original function
    print("Hello!")


# Call the decorated function
say_hello()

# Decorator Commons

# `@classmethod` - Decorator that allows a method to be called on the class itself, rather than on an instance of the class.

# `@staticmethod` - Decorator that allows a method to be called on the class itself, without using any instance-specific data.

# `@property` - Decorator that allows you to define a method as a "getter" for a class attribute, allowing you to access the attribute as if it were a variable.

# These decorators are not used in the code in this file, but they are commonly used in Python to modify the behavior of methods and attributes in classes.

# Here's an example of how you can use the `@property` decorator to define a "getter" for a class attribute:


class MyClassDecorator:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        print("Something is happening before the function runs")
        self.func()
        print("Something is happening after the function runs")


@MyClassDecorator
def say_hello_on_class():
    print("Calling MyClass Decorator Function!")


say_hello_on_class()


# Here's an example of how you can use the `@property` decorator to define a "getter" for a class attribute:

class myClass:

    value = 10

    def __init__(self, name) -> None:
        self.name = name  # Instance attribute

    def method_instance(self):  # Need a instance to be called
        return f"Instance Method: {self.name}"

    @classmethod
    def method_class(cls):  # Can be called without instance using the attribute of the class (cls)
        return f"Class Method: {cls.value}"

    @staticmethod
    def method_static():  # Can be called without instance
        return "Static Method"


# Usage
obj = myClass("Example Class")

print(obj.method_instance())  # Need a instance to be called
print(obj.method_class())  # Can be called without instance
print(obj.method_static())  # Can be called without instance
print(obj.value)  # Can be called without instance


# Here's an example of how you can use the `@property` decorator to define a "getter" for a class attribute:

class Car:
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    @classmethod
    def create_car(cls, setup):
        brand, model, year = setup.split(",")
        return cls(brand, model, int(year))


setup_toyota = "Toyota, Corolla,2022"
car_01 = Car.create_car(setup=setup_toyota)
print(f"Marca:{car_01.brand}\nModelo:{car_01.model}\nAno:{car_01.year}")


class Mathematic:
    @staticmethod
    def sum_numbers(x: int, y: int) -> int:
        return x + y


print(Mathematic.sum_numbers(x=10, y=15))
