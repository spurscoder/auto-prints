
import subprocess
import fire
import os

import glob


def merge1(path, res_path):
    res_d = {}
    for i, line in enumerate(open(res_path)):
        line = line.replace(r"/", "_")
        res_d[line.strip()] = i + 1

    files = glob.glob("./{}/*.pdf".format(path))
    for f in files:
        parts = f.split('_')
        if len(parts) < 2:
            continue

        lidx = f.find("_")
        ridx = f.rfind("_")

        name = f[lidx + 1: ridx]
        idx = 0
        if name in res_d:
            idx = res_d[name]
            print(name, idx)
        else:
            print(">>", name)
            print(">>", f)
            break

        file_name = "./{}/{}-{}".format(path, idx, name)
        if not os.path.exists(file_name):
            os.mkdir(file_name)

        subprocess.run(["cp", f, "{}/{}".format(file_name, f.split('/')[-1])])


def merge(path, res_path):
    res_d = {}
    for i, line in enumerate(open(res_path)):
        res_d[line.strip()] = i + 1

    files = glob.glob("./outputs-tmp/*.pdf")
    for f in files:
        parts = f.split('_')
        if len(parts) < 2:
            continue

        name = parts[1]
        idx = 0
        if name in res_d:
            idx = res_d[name]
        else:
            print(name)
            print(f)
            break

        file_name = "./{}/{}-{}".format("outputs-tmp", idx, name)
        if not os.path.exists(file_name):
            os.mkdir(file_name)

        subprocess.run(["cp", f, "{}/{}".format(file_name, f.split('/')[-1])])


if __name__ == "__main__":
    fire.Fire()
