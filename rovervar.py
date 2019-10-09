#---------------------------Standardied variable type containing network identifier and value--------------------
#ALL ROVER VALUES MUST BE INTEGER OR FLOAT IN ORDER TO ALLOW COMPARISON UNLESS COMPARATOR IS CHANGED
class RoverVar():
    def __init__(self,val,name):
        self.value = val
        self.name = name
