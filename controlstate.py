# class to function as both variables for rover and nodes in the tree
class TreeNode():
    def __init__(self,name):
        self.left = None
        self.right = None
        self.value = 0
        self.name = name

#Control state class to hold all variables for the rover
class ControlState():
    def __init__(self):
        self.nodes = []
        self.root = None
        self.network_string = ""

    def create_tree(self):
        self.define_robot_vars()
        self.nodes  = sorted(self.nodes, key=lambda k: k.name)  #sort names just for a nice tidy tree :) (but technically unrequired)
        prepared_nodes = cut_and_order(self.nodes)
        self.root = prepared_nodes[0]
        prepared_nodes = prepared_nodes[1:]


        for node in prepared_nodes:
            traverse_and_create(self.root,node)


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


#-----------------------------------------------------------SEARCH AND REPLACE FUNCTION FOR BINARY TREE--------------------------------------------------------
def find_replace(node,name,value = None):
    #base case when the node is found
    print(node.name,name)
    if node.name == name:
        if value == None:
            output = node.value  #if in find mode
            return output
        else:
            node.value = value  #if in replace mode
            return

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
    for name in new_state.names:
        old_val = find_replace(old_state.root,name)
        new_val = find_replace(new_state.root,name)
        differential = old_val - new_val
        find_replace(old_state.root,name,new_val)
        find_replace(new_state.root,name,differential)

#----------------------------------------------------------------PREPARE LIST FOR TREE CREATION-----------------------------------------------------------------
def cut_and_order(input_list):
    output_list = []
    if len(input_list) <= 2:
        return input_list

    middle = int(len(input_list)/2)
    left_list = input_list[:middle]
    right_list = input_list[middle+1:]

    middle = [input_list[middle]]

    output_list += cut_and_order(left_list)
    output_list += cut_and_order(right_list)

    return middle+output_list




control_state_new = ControlState()
control_state_new.create_tree()

control_state_old = ControlState()
control_state_old.create_tree()

calculate_state_differential(control_state_new,control_state_old)
