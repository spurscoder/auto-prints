import os
import subprocess
import fire
import re


def copy_01(f):
    src = "./1-锐仕方达人才科技集团有限公司.pdf"
    for line in open(f):
        idx, name = line.strip().split('\t')
        if "锐仕方达" not in name:
            print("{}-{}".format(idx, name))
            continue

        tgt = "./{}-{}.pdf".format(idx, name)
        subprocess.run(['cp', src, tgt])


def find_loss(*files):
    l = []
    for f in files:
        parts = f.strip().split('-')
        if len(parts) != 2:
            print(f)
            return

        idx = parts[0]
        l.append(int(idx))
    l_s = sorted(l)
    l = l_s[0]
    for r in l_s[1:]:
        while l + 1 < r:
            print(l + 1)
            l += 1
        l = r


def cp(*files):
    print(files)
    for f in files:
        print()
        print("---------- {} ----------".format(f))
        lines = open(f).read().strip().split('\n')
        src = lines[0]
        src = re.sub("\t", "-", src)
        if not os.path.exists("{}.pdf".format(src)):
            print("{}.pdf not exists".format(src))
            return
        for tgt in lines[1:]:
            if not tgt:
                continue
            tgt = re.sub("\t", "-", tgt)
            if src == tgt:
                continue
            print(src, tgt)
            subprocess.run(['cp', '{}.pdf'.format(src), '{}.pdf'.format(tgt)])


if __name__ == "__main__":
    fire.Fire()
