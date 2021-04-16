import random

import battlefield


class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = input("Enter Type of Dino")
        self.energy = 0
        self.attack_power = random.randint(5,10)
        self.health = 0

    def attack(self, target):
        print("dino1 is attacking robot1")
        x = self.energy / 50
        y = self.attack_power
        z = x * y
        print(self.energy)
        self.energy -= 10
        print(self.energy)
        print(target.health)
        target.health = target.health - z
        print(target.health)

        print(x,y, z)

