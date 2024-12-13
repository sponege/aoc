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

towels = lines[0].split(', ')

lines=lines[2:]
from collections import deque
from functools import cache

@cache
def find(t):
    total = 0
    if len(t) == 0: return 1
    for tt in towels:
        if t.startswith(tt): total += find(t[len(tt):])
    return total

for towel in lines:
    ans += find(towel)

print(f'ans:{ans}')
