import os

import pyperclip
from pynput.keyboard import Key

from .utils import *

from .keyboard import keyboard


def neris_csrc_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    # 按照网站具体操作
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("a"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.esc); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)

    # 因为需要验证码
    input("Press Enter.....")

    with keyboard.pressed(Key.alt):
        push_pop("`"); time.sleep(SHORT_S)

    # 打印
    do_print(filename)

    with keyboard.pressed(Key.cmd):
        push_pop("w")
    return False


def www_neeq_com_cn(it, name, check, url, output_dir):
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("c"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.esc); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("s"); time.sleep(HALF_S)
    push_pop("c"); time.sleep(3)

    do_print(filename)
    return False


def www_sse_com_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    # 按照网站的操作顺序，如下
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("s"); time.sleep(SHORT_S)
    push_pop("g"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.enter); time.sleep(3)

    # 打印
    do_print(filename)
    return False


def www_szse_cn(it, name, check, url, output_dir):
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("a"); time.sleep(SHORT_S)
    push_pop("c"); time.sleep(2)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.enter); time.sleep(3)

    do_print(filename)
    return False


def www_china_arbitration_com(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_url_search(it, name, url, output_dir):
        return True
    
    time.sleep(2)

    do_print(filename)
    return False

def www_customs_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_url_search(it, name, url, output_dir):
        return True
    
    time.sleep(2)

    do_print(filename)
    return False

def wenshu_court_gov_cn(it, name, check, url, output_dir):
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True
    return False


def zxgk_court_gov_cn_shixin(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    time.sleep(2)
    # 按照网站具体操作
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("l"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.esc); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("a"); time.sleep(SHORT_S)
    push_pop("s"); time.sleep(SHORT_S)

    # 因为需要验证码
    input("Press Enter.....")

    with keyboard.pressed(Key.alt):
        push_pop("`"); time.sleep(SHORT_S)

    # 打印
    do_print(filename)
    return False


def zxgk_court_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    # 按照网站具体操作
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("d"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.esc); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("k"); time.sleep(SHORT_S)

    # 因为需要验证码
    input("Press Enter.....")

    with keyboard.pressed(Key.alt):
        push_pop("`"); time.sleep(SHORT_S)

    # 打印
    do_print(filename)
    return False


def www_12309_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("a"); time.sleep(SHORT_S)
    push_pop("a"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.enter); time.sleep(3)

    do_print(filename)
    return False


def www_baidu_com_new(it, name, check, url, output_dir):
    # 跳到chrome
    pit = it.replace(r"/", "_")
    print(pit)

    e = []
    for page in range(5):
        filename = "{}_{}_{}".format(name, pit, page+1)
        if os.path.exists("{}/{}.pdf".format(output_dir, filename)):
            print("exists: {}/{}.pdf".format(output_dir, filename))
            e.append(True)
        else:
            e.append(False)

    if all(e):
        return True
    else:
        for page in range(5):
            filename = "{}_{}_{}".format(name, pit, page+1)
            if os.path.exists("{}/{}.pdf".format(output_dir, filename)):
                os.remove("{}/{}.pdf".format(output_dir, filename))

    with keyboard.pressed(Key.alt):
        push_pop("`")
        time.sleep(HALF_S)

    for page in range(5):
        filename = "{}_{}_{}".format(name, pit, page+1)
        with keyboard.pressed(Key.cmd):
            push_pop("t")
            time.sleep(HALF_S)
        paste(url + "wd={}&oq={}&pn={}".format(it, it, page*50))
        push_pop(Key.enter)
        time.sleep(HALF_S)

    for page in range(4):
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.shift)
            keyboard.press(Key.tab)
            time.sleep(HALF_S)
            keyboard.release(Key.shift)
            keyboard.release(Key.tab)
            time.sleep(HALF_S)

    time.sleep(2)
    for i in range(5):
        filename = "{}_{}_{}".format(name, pit, i+1)
        print(filename)

        with keyboard.pressed(Key.cmd):
            push_pop("p")
            print(1)
            time.sleep(5)

        push_pop(Key.enter)
        print(2)
        time.sleep(2.5)
        paste(filename)
        time.sleep(2.5)
        push_pop(Key.enter)
        print(3)
        time.sleep(6)

        with keyboard.pressed(Key.cmd):
            push_pop("w")
            #  push_pop(Key.tab)
        time.sleep(3)

    return False


def www_baidu_com(it, name, check, url, output_dir):
    # 跳到chrome
    for page in range(5):
        filename = "{}_{}_{}".format(name, it, page+1)
        if not start_url_search_baidu(it, name, url, output_dir, page):
            continue

        time.sleep(3)

        do_print(filename, 3)

    return False


def www_qcc_com(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    # 按照网站具体操作
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("s"); time.sleep(SHORT_S)
    push_pop("e"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.enter); time.sleep(SHORT_S)

    # 因为需要验证码
    input("Press Enter.....")
    return False


def www_gsxt_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True
    return False


def www_chinatax_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("e"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.enter); time.sleep(3)

    do_print(filename)
    return False


def www_creditchina_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    # 按照网站具体操作
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("s"); time.sleep(SHORT_S)
    push_pop("c"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.enter); time.sleep(SHORT_S)

    # 因为需要验证码
    input("Press Enter.....")
    return False


def zlxy_ancc_org_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True
    return False

def www_mee_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_url_search(it, name, url, output_dir):
        return True
    
    time.sleep(2)

    do_print(filename)
    return False


def www_csrc_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    push_pop("f"); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("a"); time.sleep(SHORT_S)
    with keyboard.pressed(Key.cmd):
        push_pop("a")
        time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.enter); time.sleep(3)

    do_print(filename)
    return False


def www_safe_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_url_search(it, name, url, output_dir):
        return True

    # push_pop("f"); time.sleep(SHORT_S)
    # push_pop("c"); time.sleep(SHORT_S)
    # paste(it); time.sleep(SHORT_S)
    # push_pop(Key.enter); 
    time.sleep(3)

    do_print(filename)
    return False

def credit_customs_gov_cn(it, name, check, url, output_dir):
    # 跳到chrome
    filename = "{}_{}".format(name, it)
    if not start_pos(it, name, url, output_dir):
        return True

    # 按照网站具体操作
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("a"); time.sleep(SHORT_S)
    paste(it); time.sleep(SHORT_S)
    push_pop(Key.esc); time.sleep(SHORT_S)
    push_pop("f"); time.sleep(SHORT_S)
    push_pop("d"); time.sleep(SHORT_S)

    # 因为需要验证码
    input("Press Enter.....")

    with keyboard.pressed(Key.alt):
        push_pop("`"); time.sleep(SHORT_S)

    # 打印
    do_print(filename)
    return False


