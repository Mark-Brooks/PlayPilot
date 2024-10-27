# main.py
from ui_manager import UIManager
from controls import RotaryEncoder
import sys

def main():
    # Initialize UI
    ui = UIManager()
    
    # Initialize rotary encoder for navigation
    rotary_encoder = RotaryEncoder(callback=ui.handle_navigation)
    
    # Run the UI main loop
    try:
        ui.run()
    except KeyboardInterrupt:
        print("Exiting application.")
        sys.exit(0)

if __name__ == "__main__":
    main()
