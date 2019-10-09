from arm import *
from drivetrain import *
import time

EXCEPTIONS = [str,list,bool,dict]       #data types to be excepted when comparing

class controlState():
    def __init__(self):
        self.drivetrain = drivetrain()
        self.arm = arm()

#COMMENTS TO BE ADDED XD
def formatForSending(state):
    networkString = ""
    attributes = list(vars(state).keys())
    
    for attributeNum in range(len(attributes)):
        currAttribute = getattr(state, attributes[attributeNum])
        attrType = type(currAttribute)
        
        if not isinstance(currAttribute, roverVar):
            networkString += formatForSending(currAttribute)
            
        elif attrType != str:
            networkString += currAttribute.name+str(currAttribute.value)+","
            
    return networkString


def calcStateDifferential(stateA,stateB):
    #gets a list containing all attribute identifiers for stateA (and therefore stateB as they are instances of the same class)
    attributes = list(vars(stateA).keys())
    
    #for each attribute identifier
    for attributeNum in range (len(attributes)):    
        
        currAttribute = getattr(stateA, attributes[attributeNum])#current attribute (so that we dont repeat too much code)
        attrType = type(currAttribute) #gets type of attribute e.g. int, roverVar, str, etc.
        
        #if attribute is not a roverVar and is a userObject
        if not isinstance(currAttribute, roverVar) and attrType not in EXCEPTIONS: 
            calcStateDifferential(currAttribute,getattr(stateB,attributes[attributeNum])) #recurse for found object
            
        #if attribute contains data we want to compare i.e. is a float or int in a roverVar
        else: 
            differential = currAttribute.value - getattr(stateB,attributes[attributeNum]).value #calculates the difference
            currAttribute.value = differential #sets the value of the attribute to the differential
            setattr(stateA,attributes[attributeNum],currAttribute) #redefines the attribute to the new value

            
#testing
stA = controlState()
stB = controlState()

stB.arm.armX.value = 5

calcStateDifferential(stA,stB)

print(stA.arm.armX.value)

