from rovervar import *
#------------------------------------Example of Drivetrain variables--------------------------------------------------

class Drivetrain():
    def __init__(self):
        self.left_power = RoverVar(0,"lp")
        self.right_power = RoverVar(0,"rp")
