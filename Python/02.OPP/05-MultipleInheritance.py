from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


# Mammal class
class Mammal(Animal):
    def make_sound(self):
        print("Mammal sound (generic)")

    def move(self):
        print("Walking or running")


# Bird class
class Bird(Animal):
    def make_sound(self):
        print("Bird sound (generic)")

    def move(self):
        print("Flying in the sky")


# Dog class
class Dog(Mammal):
    def make_sound(self):
        print("Woof woof")


# Parrot class
class Parrot(Bird):
    def make_sound(self):
        print("Squawk! I'm a parrot")


# Bat class - multiple inheritance
class Bat(Mammal, Bird):
    def make_sound(self):
        print("Screech!")

    # custom move to combine abilities
    def move(self):
        print("Can walk and fly")


# ===== Usage =====
animals = [Dog(), Parrot(), Bat()]

for animal in animals:
    animal.make_sound()
    animal.move()
    print("---")