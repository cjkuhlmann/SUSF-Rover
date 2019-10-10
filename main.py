from controlstate import *
from arm import *
from drivetrain import *
from rovervar import *
from controller import *

ps4_controller = Controller()
control_state_a = ControlState()
control_state_b = ControlState()
ps4_controller.linked_to_control_state(control_state_a)



def update():
    ps4_controller.update()
    ps4_controller.set_linked_control_state()
    calc_state_differential(control_state_a,control_state_b) #calculates differential where a is the new state
    overwrite_control_state(control_state_b,control_state_a) #replaces b's values with a's so that b will continue to be the old state
