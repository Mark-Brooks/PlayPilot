# main.py
from auth import authorize_user
from spotify_client import SpotifyClient
from display import Display
from input_handler import InputHandler

def main():
    # Initialize modules
    auth_token = authorize_user()
    spotify = SpotifyClient(auth_token)
    display = Display()
    input_handler = InputHandler(spotify, display)
    
    # Main event loop
    while True:
        display.update()         # Refresh display with current track info
        input_handler.listen()   # Listen for user input (rotary, touch)
        # You could add sleep here if performance permits to reduce CPU usage.

if __name__ == "__main__":
    main()
