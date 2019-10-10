from rovervar import *
#--------------------------------example of arm variable--------------------------------------
class Arm():
    def __init__(self):
        self.grabber_power = RoverVar(0,"gp")
        self.arm_x = RoverVar(0,"ax")
        self.arm_y = RoverVar(0,"ay")
        self.arm_z = RoverVar(0,"az")
        
