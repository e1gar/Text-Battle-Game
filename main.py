import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            if not self.player.is_alive():
                print(f"{self.computer.name} побеждает!")
                break

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
