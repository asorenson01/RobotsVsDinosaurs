import random

import battlefield


class Dinosaur:
    def __init__(self):
        self.type = self.dino_type()
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

    def dino_type(self):
        print("Lets Select what type of dinosaur this will be")
        print("Press 1 for Tyrannosaurs Rex, Press 2 for Carnotaurus, Press 3 for Raptor, Press 4 for Brontosaurus ")
        x = int(input("Enter Selection"))
        if( x == 1 ):
            y = random.randint(8,10)
            self.attack_power = y
            return "Tyrannosaurus"
        elif ( x == 2 ):

            return "Carnotaurs"
        elif ( x == 3):

            return "Raptor"
        elif (x ==4):

            return "Brontosaurus"


