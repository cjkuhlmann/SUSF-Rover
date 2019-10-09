from arm import *
from drivetrain import *
import time

EXCEPTIONS = [str,list,bool,dict]       #data types to be excepted when comparing

class ControlState():
    def __init__(self):
        self.drivetrain = Drivetrain()
        self.arm = Arm()

        
        
#------------------------------------------------------------NETWORK ENCODER---------------------------------------------------------
#COMMENTS TO BE ADDED XD

def format_for_sending(state):
    network_string = ""
    attributes = list(vars(state).keys())
    
    for attribute_num in range(len(attributes)):
        curr_attribute = getattr(state, attributes[attribute_num])
        attr_type = type(curr_attribute)
        
        if not isinstance(curr_attribute, RoverVar):
            network_string += format_for_sending(curr_attribute)
            
        elif attr_type != str:
            network_string += curr_attribute.name + str(curr_attribute.value) + ","
            
    return network_string





#--------------------------------------------------------DIFFERENTIAL CALCULATOR-----------------------------------------------------

def calc_state_differential(state_a,state_b):
    #gets a list containing all attribute identifiers for state_a (and therefore state_b as they are instances of the same class)
    attributes = list(vars(state_a).keys())
    
    #for each attribute identifier
    for attribute_num in range (len(attributes)):    
        
        curr_attribute = getattr(state_a, attributes[attribute_num])#gets the CONTENTS of the current attribute
        attr_type = type(curr_attribute) #gets type of attribute e.g. int, roverVar, str, etc.
        
        #if attribute is not a roverVar and is a userObject
        if not isinstance(curr_attribute, RoverVar) and attr_type not in EXCEPTIONS: 
            calc_state_differential(curr_attribute,getattr(state_b,attributes[attribute_num])) #recurse for found object
            
        #if attribute contains data we want to compare i.e. is a float or int in a roverVar
        else: 
            differential = curr_attribute.value - getattr(state_b,attributes[attribute_num]).value #calculates the difference
            curr_attribute.value = differential #sets the value of the attribute to the differential
            setattr(state_a,attributes[attribute_num],curr_attribute) #redefines the attribute to the new value

            
            
            
            
            
#---------------------------------------------------------------TESTING--------------------------------------------------------------
st_a = ControlState()
st_b = ControlState()

st_b.arm.arm_x.value = 5

calc_state_differential(st_a,st_b)

print(st_a.arm.arm_x.value)

