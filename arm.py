from rovervar import *
#--------------------------------example of arm variable--------------------------------------
class Arm():
    def __init__(self):
        self.grabber_power = Rover_Var(0,"gp")
        self.armX = Rover_Var(0,"ax")
        self.armY = Rover_Var(0,"ay")
        self.armZ = Rover_Var(0,"az")
        
