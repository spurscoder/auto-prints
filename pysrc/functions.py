import os

import pyperclip
from pynput.keyboard import Key

from .utils import *

from .keyboard import keyboard


def neris_csrc_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("a"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.esc); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)

    input("Press Enter.....")

    with keyboard.pressed(Key.alt):
        push_pop("`"); time.sleep(SHORT_S)

    do_print(filename)

    with keyboard.pressed(Key.cmd):
        push_pop("w")


def www_neeq_com_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("c"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.esc); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("s"); time.sleep(HALF_S)
    push_pop("c"); time.sleep(HALF_S)

    do_print(filename)


def www_sse_com_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("d"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.enter); time.sleep(LONG_S)

    do_print(filename)


def www_szse_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("s"); time.sleep(SHORT_S)
    push_pop("d"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.enter); time.sleep(LONG_S)

    do_print(filename)


def www_china_arbitration_com(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("s"); time.sleep(SHORT_S)
    push_pop("j"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.esc); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("k"); time.sleep(LONG_S)

    do_print(filename)


def wenshu_court_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def zxgk_court_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def zxgk_court_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def www_12309_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def www_baidu_com(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def www_qcc_com(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def www_gsxt_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def www_chinatax_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def www_creditchina_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def zlxy_ancc_org_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def www_safe_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


def credit_customs_gov_cn(it, name, check, url, output_dir):
    if not start_pos(it, name, url, output_dir):
        return


