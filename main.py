
import re
import sys
import json
import time

from pysrc.functions import *
from pysrc.utils import *


def print_func(items, urls, output_dir):
    for url_map in urls:
        for name, url_info in url_map.items():
            print("=" * 10)
            print()
            print("Using {}".format(name))

            url = url_info["url"]
            func = eval(url_info["func"])
            check = url_info["check"]
            for it in items:
                print("Searching {} @ {}".format(it, name))
                if func(it, name, check, url, output_dir):
                    # time.sleep(HALF_S)
                    continue
                time.sleep(LONG_S)


def read_url(path):
    urls = []
    for line in open(path):
        urls.append(json.loads(line.strip()))
    return urls


def read_items(path):
    return open(path).read().strip().split('\n')


def main(args):
    url_map = read_url(args.url)
    items = read_items(args.items)
    print_func(items, url_map, args.output_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--items", required=True, type=str, default="", help="xlsx data path")
    parser.add_argument("--url", required=True, type=str, default="./resources/url.json", help="url.txt data path")
    parser.add_argument("--output-dir", required=True, type=str, default="./outputs/", help="url.txt data path")
    args = parser.parse_args()

    print(args)

    main(args)
