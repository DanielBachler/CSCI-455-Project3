import tkinter as tk
from maestro import Controller

MOTORS_FORWARD = 0
MOTORS_TURN = 1
WAIST_TURN = 2
HEAD_TURN = 3
HEAD_TILT = 4
move_increment = 100
turn_increment = 100
waist_increment = 600
head_increment = 200
head_tilt_increment = 200

keys_dict = {
    "up":[98, 111],
    "down":[104, 116],
    "right":[102, 114],
    "left":[100, 113],
    "stop":[65],
    "turn-stop":[60],
    "waist-right":[40],
    "waist-left":[38],
    "waist-center":[39],
    "head-right":[24],
    "head-left":[26],
    "head-center":[25],
    "head-tilt-up":[52],
    "head-tilt-down":[54],
    "head-tilt-center":[53]
    }


class KeyControl():
    def __init__(self,win):
        self.root = win
        self.tango = Controller()
        print(self.tango)
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000
        
    def arrow(self, key):
        print(key.keycode)
        # Forward
        if int(key.keycode) in keys_dict["up"]:
            self.motors -= move_increment
            if(self.motors <= 1000):
                self.motors = 1000
            print("Forward")
            print(self.motors)
            self.tango.setTarget(MOTORS_FORWARD, self.motors)
        # Backward
        if key.keycode in keys_dict["down"]:
            self.motors += move_increment
            if(self.motors >= 8000):
                self.motors = 8000
            print("Backward")
            print(self.motors)
            self.tango.setTarget(MOTORS_FORWARD, self.motors)
        # Left
        if key.keycode in keys_dict["left"]:
            self.turn += turn_increment
            if(self.turn > 8000):
                self.turn = 8000
            print("Left")
            print(self.turn)
            self.tango.setTarget(MOTORS_TURN, self.turn)
        # Right
        if key.keycode in keys_dict["right"]:
            self.turn -= turn_increment
            if(self.turn < 1000):
                self.turn = 1000
            print("Right")
            print(self.turn)
            self.tango.setTarget(MOTORS_TURN, self.turn)
        # Stop
        if key.keycode in keys_dict["stop"]:
            print("Stop")
            self.motors = 6000
            self.turn = 6000
            self.tango.setTarget(MOTORS_FORWARD, self.motors)
            self.tango.setTarget(MOTORS_TURN, self.turn)
        # Turn-stop
        if key.keycode in keys_dict["turn-stop"]:
            print("Turn-stop")
            self.turn = 6000
            self.tango.setTarget(MOTORS_TURN, self.turn)
        # Waist left
        if key.keycode in keys_dict["waist-left"]:
            self.body += waist_increment
            if(self.body > 8000):
                self.body = 8000
            print(self.body)
            self.tango.setTarget(WAIST_TURN, self.body)
        # Waist right
        if key.keycode in keys_dict["waist-right"]:
            self.body -= waist_increment
            if(self.body < 1000):
                self.body = 1000
            print(self.body)
            self.tango.setTarget(WAIST_TURN, self.body)
        # Waist center
        if key.keycode in keys_dict["waist-center"]:
            self.body = 6000
            print(self.motors)
            self.tango.setTarget(WAIST_TURN, self.body)
        # Head left
        if key.keycode in keys_dict["head-left"]:
            self.headTurn += head_increment
            if self.headTurn > 8000:
                self.headTurn = 8000
            print(self.headTurn)
            self.tango.setTarget(HEAD_TURN, self.headTurn)
        # Head right
        if key.keycode in keys_dict["head-right"]:
            self.headTurn -= head_increment
            if self.headTurn < 1000:
                self.headTurn = 1000
            print(self.headTurn)
            self.tango.setTarget(HEAD_TURN, self.headTurn)
        # Head center
        if key.keycode in keys_dict["head-center"]:
            self.headTurn = 6000
            print(self.headTurn)
            self.tango.setTarget(HEAD_TURN, self.headTurn)
        # Head tilt up
        if key.keycode in keys_dict["head-tilt-up"]:
            self.headTilt += head_tilt_increment
            if self.headTilt > 8000:
                self.headTilt = 8000
            print(self.headTilt)
            self.tango.setTarget(HEAD_TILT, self.headTilt)
        # Head tilt down
        if key.keycode in keys_dict["head-tilt-down"]:
            self.headTilt -= head_tilt_increment
            if self.headTilt < 1000:
                self.headTilt = 1000
            print(self.headTilt)
            self.tango.setTarget(HEAD_TILT, self.headTilt)
        # Head tilt center
        if key.keycode in keys_dict["head-tilt-center"]:
            self.headTilt = 6000
            print(self.headTilt)
            self.tango.setTarget(HEAD_TILT, self.headTilt)



def keyboardControl():
    win = tk.Tk()
    keys = KeyControl(win)
    # Drive
    win.bind('<Up>', keys.arrow)
    win.bind('<Down>', keys.arrow)
    win.bind('<Right>', keys.arrow)
    win.bind('<Left>', keys.arrow)
    # Waist
    win.bind('<a>', keys.arrow)
    win.bind('<s>', keys.arrow)
    win.bind('<d>', keys.arrow)
    # Stops
    win.bind('<space>', keys.arrow)
    win.bind('<period>', keys.arrow)
    # Head rotate
    win.bind('<q>', keys.arrow)
    win.bind('<w>', keys.arrow)
    win.bind('<e>', keys.arrow)
    # Head tilt
    win.bind('<z>', keys.arrow)
    win.bind('<x>', keys.arrow)
    win.bind('<c>', keys.arrow)
    win.mainloop()

class NetworkControl:
    def __init__(self):
        self.tango = Controller()
        print(self.tango)
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000
        
    def control(self, code):
        # Forward
        if code in keys_dict["up"]:
            self.motors -= move_increment
            if(self.motors <= 1000):
                self.motors = 1000
            print("Forward")
            print(self.motors)
            self.tango.setTarget(MOTORS_FORWARD, self.motors)
        # Backward
        if code in keys_dict["down"]:
            self.motors += move_increment
            if(self.motors >= 8000):
                self.motors = 8000
            print("Backward")
            print(self.motors)
            self.tango.setTarget(MOTORS_FORWARD, self.motors)
        # Left
        if code in keys_dict["left"]:
            self.turn += turn_increment
            if(self.turn > 8000):
                self.turn = 8000
            print("Left")
            print(self.turn)
            self.tango.setTarget(MOTORS_TURN, self.turn)
        # Right
        if code in keys_dict["right"]:
            self.turn -= turn_increment
            if(self.turn < 1000):
                self.turn = 1000
            print("Right")
            print(self.turn)
            self.tango.setTarget(MOTORS_TURN, self.turn)
        # Stop
        if code in keys_dict["stop"]:
            print("Stop")
            self.motors = 6000
            self.turn = 6000
            self.tango.setTarget(MOTORS_FORWARD, self.motors)
            self.tango.setTarget(MOTORS_TURN, self.turn)
        # Turn-stop
        if code in keys_dict["turn-stop"]:
            print("Turn-stop")
            self.turn = 6000
            self.tango.setTarget(MOTORS_TURN, self.turn)
        # Waist left
        if code in keys_dict["waist-left"]:
            self.body += waist_increment
            if(self.body > 8000):
                self.body = 8000
            print(self.body)
            self.tango.setTarget(WAIST_TURN, self.body)
        # Waist right
        if code in keys_dict["waist-right"]:
            self.body -= waist_increment
            if(self.body < 1000):
                self.body = 1000
            print(self.body)
            self.tango.setTarget(WAIST_TURN, self.body)
        # Waist center
        if code in keys_dict["waist-center"]:
            self.body = 6000
            print(self.motors)
            self.tango.setTarget(WAIST_TURN, self.body)
        # Head left
        if code in keys_dict["head-left"]:
            self.headTurn += head_increment
            if self.headTurn > 8000:
                self.headTurn = 8000
            print(self.headTurn)
            self.tango.setTarget(HEAD_TURN, self.headTurn)
        # Head right
        if code in keys_dict["head-right"]:
            self.headTurn -= head_increment
            if self.headTurn < 1000:
                self.headTurn = 1000
            print(self.headTurn)
            self.tango.setTarget(HEAD_TURN, self.headTurn)
        # Head center
        if code in keys_dict["head-center"]:
            self.headTurn = 6000
            print(self.headTurn)
            self.tango.setTarget(HEAD_TURN, self.headTurn)
        # Head tilt up
        if code in keys_dict["head-tilt-up"]:
            self.headTilt += head_tilt_increment
            if self.headTilt > 8000:
                self.headTilt = 8000
            print(self.headTilt)
            self.tango.setTarget(HEAD_TILT, self.headTilt)
        # Head tilt down
        if code in keys_dict["head-tilt-down"]:
            self.headTilt -= head_tilt_increment
            if self.headTilt < 1000:
                self.headTilt = 1000
            print(self.headTilt)
            self.tango.setTarget(HEAD_TILT, self.headTilt)
        # Head tilt center
        if code in keys_dict["head-tilt-center"]:
            self.headTilt = 6000
            print(self.headTilt)
            self.tango.setTarget(HEAD_TILT, self.headTilt)

    