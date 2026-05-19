# POO
""""

- **Class**: A blueprint for creating objects. Defines the attributes and behavior of objects.
- **Object**: An instance of a class. Has its own set of attributes and behavior.
- **Attribute**: A variable inside a class that stores data.
- **Method**: A function inside a class that defines the behavior of objects.

I hope this helps! Let me know if you have any other questions.
"""

# Class - > Model and template for creating objects
# Object - > Instance of a class
# Attribute - > Variables inside a class
# Method - > Function inside a class

class Person:
    # Constructor
    def __init__(self, name: str, age: int) -> None:
        # Attributes
        self.name = name  # Variable that stores the person's name
        self.age = age  # Variable that stores the person's age

    # Method
    def greetings(self) -> str:
        """
        Returns a string with the person's name and age
        """
        return f"Hello, my name is {self.name} and I'm {self.age} years old"

# Object 1
person1 = Person("Donny", 20)

# Object 2
person2 = Person("Ricardo", 30)

# Print out the attributes of person1
print(person1.name, person1.age, sep=" | ")

# Print out the greeting of person1
mensagem = person1.greetings()
print(mensagem)

# Print out the attributes of person2
print(person2.name, person2.age, sep=" | ")

 