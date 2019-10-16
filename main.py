from controlstate import *
from controller import *

ps4_controller = Controller()
control_state_new = ControlState()
control_state_old = ControlState()
ps4_controller.linked_to_control_state(control_state_a)



def update():
    ps4_controller.update()
    ps4_controller.set_linked_control_state()
    calc_state_differential(control_state_new,control_state_old) #calculates differential where a is the new state
    network_string = control_state_new.create_network_string()


