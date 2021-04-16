from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []


    def creat_herd(self, name1, attackpower1, name2, attackpower2, name3, attackpower3):
        dino1 = Dinosaur(name1, attackpower1)
        dino1.health = 100
        dino1.energy = 100
        dino2 = Dinosaur(name2, attackpower2)
        dino2.health = 100
        dino2.energy = 100
        dino3 = Dinosaur(name3, attackpower3)
        dino3.health = 100
        dino3.energy = 100
        self.dinosaurs.append(dino1)
        # self.dinosaurs.append(dino2)
        # self.dinosaurs.append(dino3)
