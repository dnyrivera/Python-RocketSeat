class Character:
    def __init__(self, name, life, level) -> None:
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name

    def get_life(self):
        return self.__life

    def get_level(self):
        return self.__level

    def get_details(self):
        return f"Name: {self.get_name()}\n Life: {self.get_life()}\n Level: {self.get_level()}\n"

    def take_damage(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0
        return self.__life

    def attack(self, target):
        damage = self.get_level() * 2
        target.take_damage(damage)
        print(
            f"{self.get_name()} is attacking {target.get_name()} and the damage is {self.get_level()}")


class Hero(Character):
    def __init__(self, name, life, level, skill):
        super().__init__(name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def get_details(self):
        return f"{super().get_details()} Habilidade: {self.get_skill()}"


class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def get_details(self):
        return f"{super().get_details()} Type: {self.get_type()}"


class Game:
    def __init__(self):
        self.hero = Hero(name='Donny', life=100, level=1, skill='Speed')
        self.enemy = Enemy(name="Bat", life=25, level=2, type='Fly')

    def start_battle(self):

        print("Start Battle")

        while (self.hero.get_life() > 0 and self.enemy.get_life() > 0):
            print("Characters Details:")
            print(self.hero.get_details())
            print(self.enemy.get_details())

            input("Press Enter to attack...")
            option = input("Choose: 1 - Normal Attack | 2 - Especial Attack")

        if self.hero.get_life() > 0:
            print("Hero Won")
        else:
            print("Enemy Won")


# Game Instance and Start Battle
game = Game()
game.start_battle()
