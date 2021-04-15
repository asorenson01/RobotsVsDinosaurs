from weapon import Weapon

class Robot:
    def __init__(self,):
        self.name = input("Input Robots Name")
        self.power_level = 0
        self.health = 0
        self.weapon = self.create_weapon()

    def create_weapon(self):
        type = input ("Select Weapon Type")
        power = 50
        weapon = Weapon(type, power)
        return weapon




 # def attack(dinosaur): #void
