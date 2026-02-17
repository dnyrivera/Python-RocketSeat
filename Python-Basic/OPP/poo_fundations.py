# Hierarchy inheritance
# Single responsibility principle

from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def walk(self) -> None:
        print(f"{self.name} is walking")

    def sound(self) -> None:
        print(f"{self.name} is making a sound")


class Dog(Animal):
    def sound(self) -> None:
        return f"{self.name} is barking"


class Cat(Animal):
    def sound(self) -> None:
        return f"{self.name} is meowing"


dog = Dog(name="Rex")
cat = Cat(name="Garfield")

print('\nPolymorphism Example')
animals = [dog, cat]

for animal in animals:
    print(animal.sound())


print('\nEncapsulation Example')


class bankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid amount or insufficient balance.")

    def get_balance(self):
        return self.__balance


account = bankAccount(1000)
# Output: Initial balance: 1000 (account.get_balance())
print(f"Initial balance: {account.get_balance()}")
account.deposit(500)
# Output: New balance: 1500 (account.get_balance())
print(f"New balance: {account.get_balance()}")
account.deposit(-500)
# Output: New balance: 1500 (account.get_balance())
print(f"New balance: {account.get_balance()}")
account.withdraw(200)
# Output: New balance: 1300 (account.get_balance())
print(f"New balance: {account.get_balance()}")
account.withdraw(15000)
# Output: New balance: 1300 (account.get_balance())
print(f"New balance: {account.get_balance()}")


print('\nAbstraction Example')
# Abstraction


class Vehicle(ABC):

    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass


class Car(Vehicle):
    def __init__(self) -> None:
        pass

    def turnOn(self):
        print("Car is turning on")

    def turnOff(self):
        print("Car is turning off")


yellow_car = Car()
yellow_car.turnOn()
yellow_car.turnOff()
