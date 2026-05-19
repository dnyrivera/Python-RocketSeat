import random
from abc import ABC, abstractmethod
from IPython.display import clear_output  # clear console output in jupyter


class Character(ABC):

    def __init__(self, name: str, life: int, level: int) -> None:
        self.__name = name
        self.__life = life
        self.__level = level

    @property
    def name(self):
        return self.__name

    @property
    def life(self):
        return self.__life

    @property
    def level(self):
        return self.__level

    @abstractmethod
    def show_details(self) -> str:
        return f"Name: {self.name}\nLife: {self.life}\nLevel: {self.level}"

    def damage(self, amount: int):
        self.__life = max(0, self.__life - amount)

    def attack(self, target: "Character"):
        hit = random.randint(self.level * 1, self.level * 3)
        target.damage(hit)
        print(f"--> {self.name} attacks {target.name} and causes {hit} damage!")


class Hero(Character):

    def __init__(self, name: str, life: int, level: int, skill: str) -> None:
        super().__init__(name, life, level)
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

    def show_details(self) -> str:
        return f"==Hero==\n{super().show_details()}\nSkill: {self.skill}"

    def special_attack(self, target: Character):
        hit = random.randint(self.level * 4, self.level * 8)
        target.damage(hit)
        print(
            f"--> {self.name} uses Special Attack on {target.name} and causes {hit} damage!")


class Enemy(Character):

    def __init__(self, name: str, life: int, level: int, type: str) -> None:
        super().__init__(name, life, level)
        self.__type = type

    @property
    def type(self):
        return self.__type

    def show_details(self) -> str:
        return f"==Enemy==\n{super().show_details()}\nType: {self.type}"


class Game:
    """Game Class to run the game and start the battle between the hero and the enemy in turns"""

    def __init__(self):
        self.hero = Hero("Hero", 100, 5, "Strong")
        self.enemy = Enemy("Bat", 50, 3, "Fly")

    def start_battle(self):
        print("\n============ Starting Battle ============\n")

        while self.hero.life > 0 and self.enemy.life > 0:
            print(self.hero.show_details())
            print(self.enemy.show_details())

            choice = input(
                "\n[1] Normal Attack\n[2] Special Attack\n[3] Run\nChoose an option: ").strip()

            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
                self.hero.special_attack(self.enemy)
            elif choice == "3":
                print("You ran away!")
                break
            else:
                print("Invalid option. Please try again.")
                continue

            if self.enemy.life > 0:
                self.enemy.attack(self.hero)

            input("\nPress Enter to continue...")
            clear_output(wait=True)

        if self.hero.life > 0 and self.enemy.life == 0:
            print("Congratulations, you won the battle!")
        elif self.hero.life == 0:
            print("Game Over - You lost the battle!")

    game = Game()
    game.start_battle()
