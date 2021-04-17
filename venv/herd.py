from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []


    def creat_herd(self):
        dino1 = Dinosaur()
        dino1.health = 100
        dino1.energy = 100
        dino2 = Dinosaur()
        dino2.health = 100
        dino2.energy = 100
        dino3 = Dinosaur()
        dino3.health = 100
        dino3.energy = 100
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
