from battlefield import Battlefield
from fleet import Fleet
from robot import Robot
from weapon import Weapon
from  herd import Herd
from dinosaur import Dinosaur

if __name__ == '__main__':
    robot1 = Robot('Ver 1.0')
    robot1.health = 100
    robot1.power_level =100
    robot2 = Robot('Ver 2.0')
    robot2.health = 100
    robot2.power_level = 100
    robot3 = Robot('Ver 3.0')
    robot2.health = 100
    robot2.power_level = 100
    robot_fleet = Fleet()


    dino1 = Dinosaur('T-Rex', 100)
    dino1.health = 100
    dino1.energy = 100
    dino2 = Dinosaur('Raptor', 100)
    dino2.health = 100
    dino2.energy = 100
    dino3 = Dinosaur('Compi', 100)
    dino3.health = 100
    dino3.energy = 100



