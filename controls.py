# controls.py
from gpiozero import RotaryEncoder, Button

class RotaryEncoder:
    def __init__(self, callback):
        self.encoder = RotaryEncoder(pin_a=17, pin_b=18)
        self.button = Button(27)
        self.callback = callback

        # Set up event handlers
        self.encoder.when_rotated_clockwise = self.rotate_clockwise
        self.encoder.when_rotated_counter_clockwise = self.rotate_counter_clockwise
        self.button.when_pressed = self.select_button

    def rotate_clockwise(self):
        self.callback("next")

    def rotate_counter_clockwise(self):
        self.callback("previous")

    def select_button(self):
        self.callback("select")
