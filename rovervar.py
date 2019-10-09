#---------------------------Standardied variable type containing network identifier and value--------------------
#ALL ROVER VALUES MUST BE INTEGER OR FLOAT IN ORDER TO ALLOW COMPARISON UNLESS COMPARATOR IS CHANGED
class RoverVar():
    def __init__(self,val,name):
        self.value = val #value to be held by the rover (FLOAT or INT)
        self.name = name #name to be used to identify the variable when sent via the network (preferably a 2-3 character identifier)
