# class to function as both variables for rover and nodes in the tree
class TreeNode():
    def __init__(self,name):
        self.left = 0
        self.right = 0
        self.value = 0
        self.name = name

#Control state class to hold all variables for the rover
class ControlState():
    def __init__(self):
        self.nodes = []
        self.root = None
        self.network_string = ""

    def create_root(self):
        self.values = sorted(self.values, key=lambda k: k.name)  #sort names just for a nice tidy tree :) (but technically unrequired)
        self.root = self.values[len(self.values)/2]

    #-----------------------------------------------------------ROBOT VARIABLE DEFINITION FUNCTION-------------------------------------------------------------
    def define_robot_vars(self):
        self.names = ["arm_up","arm_down","arm_grab", #NON-LOCAL VAR FOR GUI IMPLEMENTATION
                "left_power","right_power"]


        for name in self.names:
            self.nodes.append(TreeNode(name))

    #------------------------------------------------------------------CREATE NETWORK STRING-------------------------------------------------------------------
    #Could replace with a tree traversal e.g. in-order traversal. More efficient but would require rewriting seach or making a new function
    def create_network_string(self):
        output = ""
        for name in self.names:
            value = find_replace(self.root,name)
            if value != 0:
                output += name + "," + str(value) + ";"
            return output


    """
    def send_network_string(self):
        self.network_string = ""
        self.create_network_string(self.root)
        self.send_network_string()

    def send_mnetwork_string(self)
    #CODE TO SEND STRING TO network_string



    
    IN-ORDER SEARCH DEVELOPMENT

    def create_network_string(self,node):
        if node.left != None:
            create_network_string(self,node.left)
        if node.right != None:
            create_network_string(self,noce.right)
        self.network_string += node.name + "," + str(node.value) + ";"



    """

#-----------------------------------------------------------SEARCH AND REPLACE FUNCTION FOR BINARY TREE--------------------------------------------------------
def find_replace(node,name,value = None):
    #base case when the node is found
    if node.name == name:
        if value == None:
            output = node.value  #if in find mode
        else:
            node.value = value  #if in replace mode

    if name <= node.name:
        output = find_replace(node.left,name,value)  #carries the foudn value through the callstack
    else:
        output = find_replace(node.right,name,value)   #carries the foudn value through the callstack

    return output; #returns the found value

#---------------------------------------------------------------------CONSTRUCTION OF BINARY TREE--------------------------------------------------------------
def traverse_and_create(node,item):
    if item.name <= node.name:
        if node.left == None:
            node.left = item
        else:
            traverse_and_create(node.left,item)
    else:
        if node.right == None:
            node.right = item
        else:
            traverse_and_create(node.right,item)


#---------------------------------------------------------------------CALCULATE STATE DIFFERENTIAL--------------------------------------------------------------
#replaces values in new_state with the differentials and the values in the old state with the values in the new state
def calculate_state_differential(new_state,old_state):
    for name in self.names:
        old_val = find_replace(old_state.root,name)
        new_val = find_replace(new_state.root,name)
        differential = old_val - new_val
        find_replace(old_state.root,name,new_val)
        find_replace(new_state.root,name,differential)
