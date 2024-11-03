# input_handler.py
import RPi.GPIO as GPIO

class InputHandler:
    def __init__(self, spotify_client, display):
        self.spotify = spotify_client
        self.display = display
        # Rotary encoder GPIO setup (adjust pins as needed)
        GPIO.setmode(GPIO.BCM)
        self.encoder_clk = 17
        self.encoder_dt = 18
        GPIO.setup(self.encoder_clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.encoder_dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def listen(self):
        if GPIO.input(self.encoder_clk) == 1:
            if GPIO.input(self.encoder_dt) == 0:
                self.spotify.next_track()  # Example for rotary to next track
                track_info = self.spotify.get_current_track()
                self.display.update(track_info)
            else:
                self.spotify.pause_track()  # Example for button press to pause
