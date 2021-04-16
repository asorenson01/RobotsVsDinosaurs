import random

from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet ()
        self.herd = Herd ()

    def run_game(self):
        x = self.display_welcome()
        if (x == "Dino"):
            self.dino_turn(self)






        print("Next part dummy")

    def display_welcome(self):
        print('Welcome to Robot Vrs Dinosaurs, Shortly we will be building a fleet of Robots to battle a heard of dinosaurs.  First we need to see who will go first')
        x = int(input('Press 1 for Heads, Press 2 for Tails'))
        # y = random.randint(1,2)
        y = 2
        if (x == 1 & y == 1):
            print("We Will build the Robot Fleet first and they get first attack")
            self.robot_call_to_arms()
            print("Now you have an amazing fleet of Robots Lets get the Dinos ready to repel the attack")
            self.dino_call_to_arms()
            return "Robot"
        else:
            print("Lets go Round some Dino's, build a Herd and get them ready to attack")
            self.dino_call_to_arms()
            print("What a amazing Herd of Huge Dinos! Let go build some Robots for your Dinos to Trample ")
            self.robot_call_to_arms()
            return "Dino"

    def robot_call_to_arms(self):
        self.fleet.creat_fleet()
        i = 0
        print(f"Your Fleet consits of {len(self.fleet.robots)} Robots.")
        while i < len(self.fleet.robots):
            print(f"Lets meet them, Robot{i+1}'s Name is:{self.fleet.robots[i].name} With a {self.fleet.robots[i].weapon.type} for a Weapon, and a attack power of {self.fleet.robots[i].weapon.attack_power}")
            i += 1

    def dino_call_to_arms(self):
        self.herd.creat_herd('T-Rex', 100, 'Raptor',10 , 'Compi', 100)
        i = 0
        print(f"Your Herd consits of {len(self.herd.dinosaurs)} Dinosaurs")
        while i < len(self.herd.dinosaurs):
            print(f"Lets meet them, Dino{i+1} is a {self.herd.dinosaurs[i].type} and has an attack power of {self.herd.dinosaurs[i].attack_power}")
            i += 1

    def dino_turn(self,dino):
        turn = 0
        while turn < 3:
            print("Lets Pick a Dino to Attack!")
            i = 0
            while i < len(self.herd.dinosaurs):
                print(f"Press {i+1} for {self.herd.dinosaurs[i].type}")
                i += 1
            dino = int(input("Make Choice"))
            print("Lets Pick a Target")
            robot = int(input(f"Press 1 to Target {self.fleet.robots[0].name} Press 2 to Target {self.fleet.robots[1].name} Press 3 to Target {self.fleet.robots[2].name} "))
            self.herd.dinosaurs[dino-1].attack(self.fleet.robots[robot-1])
            turn += 1
            print(f"Hard HIT!!!{self.fleet.robots[robot-1].name}'s Health is at {self.fleet.robots[robot-1].health}% ")
            if (self.fleet.robots[robot-1].health > 0):
                print(f"{self.fleet.robots[robot-1].name}is still alive")
                x = int(input("Press 1 to reattack, Press to 2 continue"))
                if( x == 1 ):
                    self.herd.dinosaurs[dino - 1].attack(self.fleet.robots[robot - 1])
                    turn +=1
                else:
                    return
            elif (self.fleet.robots[robot-1].health <= 0):
                self.fleet.robots.remove(self.fleet.robots[robot-1])





















# def run_game(): #void

    def battle(self):

        self.herd.dinosaurs[1].attack(self.fleet.robots[0])







# def dino_turn(dinosaur): #void
#
    # def robo_turn(robot):

#
# def show_dino_opponent_option(): #void
#
# def show_robo_opponent_options(): #void
#
# def display_winner(): #void