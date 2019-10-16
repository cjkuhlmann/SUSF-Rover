class Controller():
    def __init__(self):
        
        self.linked_state = None

        self.system_values = {'ABS_Y': 0, 'ABS_X': 0, 'ABS_Z': 0, 'BTN_THUMBL': 0,  # left stick
                       'ABS_RY': 0, 'ABS_RX': 0, 'ABS_RZ': 0, 'BTN_THUMBR': 0,  # right stick
                       'BTN_TL': 0, 'BTN_TR': 0,  # bumpers
                       'ABS_HAT0X': 0, 'ABS_HAT0Y': 0,  # dpad
                       'BTN_START': 0, 'BTN_SELECT': 0,  # selectors
                       'BTN_WEST': 0, 'BTN_SOUTH': 0, 'BTN_EAST': 0, 'BTN_NORTH': 0  # buttons
                      }
        #syetem inputs converted to understandable inputs
        self.controller_values = {"left_stick_x": None,
                                "left_stick_y": None,
                                "right_stick_x": None,
                                "right_stick_x": None,
                                "btns_N": None,
                                "btns_E": None,
                                "btns_S": None,
                                "btns_W": None,
                                "dpad_N": None,
                                "dpad_E": None,
                                "dpad_S": None,
                                "dpad_W": None,
                                "left_trigger": None,
                                "left_button": None,
                                "right_trigger": None,
                                "right_button": None,
                                "start": None,
                                "select": None
                                }


        #bindings for controller
        self.control_bindings = {"left_stick_x": None,
                                 "left_stick_y": None,
                                 "right_stick_x": None,
                                 "right_stick_x": None,
                                 "btns_N": None,
                                 "btns_E": None,
                                 "btns_S": None,
                                 "btns_W": None,
                                 "dpad_N": None,
                                 "dpad_E": None,
                                 "dpad_S": None,
                                 "dpad_W": None,
                                 "left_trigger": None,
                                 "left_button": None,
                                 "right_trigger": None,
                                 "right_button": None,
                                 "start": None,
                                 "select": None
                                 }


        def linked_to_control_state(self,state):
            self.linked_state = state

        def update_linked_control_state(self,state):
            for key,value in self.controller_values:
                if value != None:
                    self.linked_state.find_replace(control_bindings[key],value)


        def update(self):
            self.update_controller()
            self.update_values()
            self.send_data_to_state()


        def update_controller(self):
            events = get_gamepad()
            for event in events:
                if event.code != "SYN_REPORT":
                    self.system_values[even.code] = even.value

        def update_values(self):
            self.controller_values["left_stick_x"] = self.system_values["ABS_X"]
            self.controller_values["left_stick_y"] = self.system_values["ABS_Y"]
            self.controller_values["right_stick_x"] = self.system_values["ABS_RX"]
            self.controller_values["right_stick_y"] = self.system_values["ABS_RY"]
            self.controller_values["btns_N"] = self.system_values["BTN_NORTH"]
            self.controller_values["btns_E"] = self.system_values["BTN_EAST"]
            self.controller_values["btns_S"] = self.system_values["BTN_SOUTH"]
            self.controller_values["btns_W"] = self.system_values["BTN_WEST"]


            self.controller_values["dpad_N"] = 0
            self.controller_values["dpad_S"] = 0
            self.controller_values["dpad_E"] = 0
            self.controller_values["dpad_W"] = 0

            if self.system_values["ABS_HAT0Y"] == 1:
                self.controller_values["dpad_N"] = 1
            elif self.system_values["ABS_HAT0Y"] == -1:
                self.controller_values["dpad_S"] = 1


            if self.system_values["ABS_HAT0X"] == 1:
                self.controller_values["dpad_E"] = 1
            elif self.system_values["ABS_HAT0X"] == -1:
                self.controller_values["dpad_W"] = 1


            self.controller_values["start"] = self.system_values["BTN_START"]
            self.controller_values["select"] = self.system_values["BTN_SELECT"]

            self.controller_values["left_trigger"] = self.system_values["ABS_Z"]
            self.controller_values["left_button"] = self.system_values["BTN_TL"]
            self.controller_values["right_trigger"] = self.system_values["ABS_RZ"]
            self.controller_values["right_button"] = self.system_values["BTN_TR"]

        def map_control(self,control,command):
            self.control_bindings[control] = command
