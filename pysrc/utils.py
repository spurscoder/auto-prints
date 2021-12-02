import os
import time

import pyperclip
from pynput.keyboard import Key

from .keyboard import keyboard


LONG_S = 2
SHORT_S = 1
HALF_S = 0.5


def push_pop(key):
    keyboard.press(key)
    keyboard.release(key)


def paste(text):
    pyperclip.copy(text)
    time.sleep(HALF_S)
    with keyboard.pressed(Key.cmd):
        push_pop("v")


def start_pos(it, name, url, output_dir):
    filename = "{}_{}".format(name, it)
    if os.path.exists("{}/{}.pdf".format(output_dir, filename)):
        print("exists: {}/{}.pdf".format(output_dir, filename))
        return False

    with keyboard.pressed(Key.alt):
        push_pop("`")
        time.sleep(SHORT_S)

    with keyboard.pressed(Key.cmd):
        push_pop("l")
        time.sleep(SHORT_S)

    paste(url)
    push_pop(Key.enter)
    time.sleep(SHORT_S)
    return True


def do_print(filename):
    with keyboard.pressed(Key.cmd):
        push_pop("p")
        time.sleep(LONG_S)

        push_pop(Key.enter)
        time.sleep(SHORT_S)

        paste(filename)
        time.sleep(HALF_S)

        push_pop(Key.enter)
