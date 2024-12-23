#!/bin/python3

# this video is sponsored by taco bell

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=0

inp=inp.strip()
print('read everything')

from collections import deque

def mix(v, sn):
    return v ^ sn

def prune(sn):
    return sn % 16777216

for t in lines:
    sn = int(t)
    for i in range(2000):
        sn = prune(mix(sn*64, sn))
        sn = mix(sn//32, sn)
        sn = prune(sn)
        sn = mix(sn*2048, sn)
        sn = prune(sn)
    if test: print(sn)
    ans += sn


print(f'ans:{ans}')
