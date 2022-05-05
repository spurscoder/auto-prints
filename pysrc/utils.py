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
    time.sleep(0.3)
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

def start_url_search(it, name, url, output_dir):
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

    paste(url+it)
    push_pop(Key.enter)
    time.sleep(SHORT_S)
    return True


def start_url_search_baidu_new(it, name, url, output_dir, page):
    filename = "{}_{}_{}".format(name, it, page+1)

    with keyboard.pressed(Key.alt):
        push_pop("`")
        time.sleep(SHORT_S)

    with keyboard.pressed(Key.cmd):
        push_pop("l")
        time.sleep(SHORT_S)

    paste(url + "wd={}&oq={}&pn={}".format(it, it, page*50))
    push_pop(Key.enter)

    time.sleep(1)

    return True


def start_url_search_baidu(it, name, url, output_dir, page):
    filename = "{}_{}_{}".format(name, it, page+1)
    if os.path.exists("{}/{}.pdf".format(output_dir, filename)):
        print("exists: {}/{}.pdf".format(output_dir, filename))
        return False

    with keyboard.pressed(Key.alt):
        push_pop("`")
        time.sleep(SHORT_S)

    with keyboard.pressed(Key.cmd):
        push_pop("l")
        time.sleep(SHORT_S)

    paste(url + "wd={}&oq={}&pn={}".format(it, it, page*50))
    push_pop(Key.enter)
    time.sleep(1)
    return True


def do_print(filename, wait=1):
    with keyboard.pressed(Key.cmd):
        push_pop("p")
        print(1)
        time.sleep(wait+2)
        push_pop(Key.enter)
        print(2)

        time.sleep(2)
        paste(filename)
        time.sleep(HALF_S)
        push_pop(Key.enter)
        print(3)
