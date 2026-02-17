# @classmethod -> don't need self
# @staticmethod -> don't need self or cls

class myClass:
    value = 10

    def __init__(self, name) -> None:
        self.name = name

    def instance_method(self):
        return f"Instance Method called : {self.name}"

    @classmethod
    def class_method(cls):
        return f"Class Method called : {cls.value}"

    @staticmethod
    def static_method():
        return f"Static Method called"


my_class = myClass("John")
print(my_class.instance_method())
print(my_class.class_method())
print(my_class.static_method())


class Car:
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    @classmethod
    def create_car(cls, setup):
        brand, model, year = setup.split(",")
        return cls(brand, model, int(year))


setup1 = "Mercedes,G63,2022"
setup2 = "Ferrari,488,2022"
setup3 = "Lamborghini,Huracan,2022"

car1 = Car.create_car(setup1)
car2 = Car.create_car(setup2)
car3 = Car.create_car(setup3)

print(f"Brand:{car1.brand}, Model:{car1.model}, Year:{car1.year}")
print(f"Brand:{car2.brand}, Model:{car2.model}, Year:{car2.year}")
print(f"Brand:{car3.brand}, Model:{car3.model}, Year:{car3.year}")


class Math:
    @staticmethod
    def sum(a, b):
        return a + b


print(Math.sum(a=1, b=2))
