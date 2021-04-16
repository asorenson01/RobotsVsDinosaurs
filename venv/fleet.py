from robot  import Robot
class Fleet:
    def __init__(self):
        self.robots = []




    def creat_fleet(self):
        robot1 = Robot()
        robot1.health = 100
        robot1.power_level = 100
        robot2 = Robot()
        robot2.health = 100
        robot2.power_level = 100
        robot3 = Robot()
        robot3.health = 100
        robot3.power_level = 100
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)



