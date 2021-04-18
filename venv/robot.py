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
        print(f"Lets select {self.name}'s weapon. Press 1 for a Sword, Press 2 for a Knife, Press 3 for a Thermonuclear Bomb, Press 4 for a Taser")
        x = int(input("Enter Selection"))
        if (x == 1):
            type = "Sword"
            attack_power = random.randint(7, 8)
        elif ( x == 2):
            type = "Knife"
            attack_power = random.randint(6, 7)
        elif ( x == 3):
            type ="Thermonuclear Bomb"
            attack_power = random.randint(10, 10)
        elif ( x ==4 ):
            type = " Taser"
            attack_power = random.randint(2, 6)
        weapon = Weapon(type, attack_power)
        return weapon


    def attack(self, target):
        print("<-------attacking-------->")
        x = self.power_level / 10
        y = self.weapon.attack_power
        z = x * y
        self.power_level -= 10
        target.health = target.health - z
