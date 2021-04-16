import random

import battlefield


class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = input("Enter Type of Dino")
        self.energy = 0
        self.attack_power = random.randint(5,10)
        self.health = 0

    def attack(self, target):
        print("<-------attacking-------->")
        x = self.energy / 10
        y = self.attack_power
        z = x * y
        self.energy -= 10
        target.health = target.health - z


