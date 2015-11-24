#!/usr/bin/env python
# coding=UTF-8

import re
import json
import sys

def filter(input):
    for line in input:
        try:
            line_deco = json.loads(line)
            print line_deco

        except:
            continue

def lines(fp):
    print str(len(fp.readlines()))

def main():
    input = open(sys.argv[1])
    output = (sys.argv[2])
    #lang = open(sys.argv[3])
    filter(input)

if __name__ == '__main__':
    main()
