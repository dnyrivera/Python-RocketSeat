class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_sound(self) -> None:
        pass


class Mammalia(Animal):
    def breast_feed(self) -> str:
        return f"{self.name} is breasting feeding"


class Aves(Animal):
    def fly(self) -> str:
        return f"{self.name} is flying"


class Bat(Aves, Mammalia):
    def make_sound(self):
        return "Chirp chirp"


bat = Bat(name="Batman")

print("Bat Name:", bat.name)
print("Bat Sound:", bat.make_sound())
print("Bat Breast Feed:", bat.breast_feed())
print("Bat Fly:", bat.fly())

# Output:
# Bat Name:  Batman
# Bat Sound:  Chirp chirp
# Bat Breast Feed:  Batman is breasting feeding
# Bat Fly:  Batman is flying
