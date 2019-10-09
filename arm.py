from rovervar import *
#--------------------------------example of arm variable--------------------------------------
class Arm():
    def __init__(self):
        self.grabber_power = Rover_Var(0,"gp")
        self.arm_x = Rover_Var(0,"ax")
        self.arm_y = Rover_Var(0,"ay")
        self.arm_z = Rover_Var(0,"az")
        
