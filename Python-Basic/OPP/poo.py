
# Example Class

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def salutation(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old")


# object
person1 = Person(name="Donny", age=42)
person1.salutation()

person2 = Person(name="Josany", age=39)
person2.salutation()
