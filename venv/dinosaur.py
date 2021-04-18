import random

import battlefield


class Dinosaur:
    def __init__(self):
        self.attack_power = 0
        self.type = self.dino_type()
        self.energy = 0
        self.health = 0

    def attack(self, target):
        print("<-------attacking-------->")
        x = self.energy / 10
        y = self.attack_power
        z = x * y
        self.energy -= 10
        target.health = target.health - z

    def dino_type(self):
        print("Lets Select what type of dinosaur this will be")
        print("Press 1 for Tyrannosaurs Rex, Press 2 for Carnotaurus, Press 3 for Raptor, Press 4 for Brontosaurus ")
        x = int(input("Enter Selection"))
        if( x == 1 ):
            self.attack_power = random.randint(9, 10)
            return "Tyrannosaurus"
        elif ( x == 2 ):
            self.attack_power = random.randint(7, 9)
            return "Carnotaurs"
        elif ( x == 3):
            self.attack_power = random.randint(6, 10)
            return "Raptor"
        elif (x ==4):
            self.attack_power = random.randint(2, 6)
            return "Brontosaurus"


