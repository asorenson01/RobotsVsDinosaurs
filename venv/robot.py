import random

import weapon
from weapon import Weapon

class Robot:
    def __init__(self,):
        self.name = input("Input Robots Name")
        self.power_level = 0
        self.health = 0
        self.weapon = self.create_weapon()

    def create_weapon(self):
        type = input ("Select Weapon Type")
        attack_power = random.randint(5,10)
        weapon = Weapon(type, attack_power)
        return weapon


def attack(self, target):
    print("<-------attacking-------->")
    x = self.energy / 10
    y = self.weapon.attack_power
    z = x * y
    self.energy -= 10
    target.health = target.health - z
