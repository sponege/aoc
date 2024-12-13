#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
pp = lambda *args: [print(*args) if test else 0]

inp=inp.strip()
# print('read everything')

stones = list(map(int, inp.split()))


ans=0
a=0
import functools

@functools.lru_cache(maxsize=None)
def getStone(s,i):
    global ans, a
    a+=1
    if i == 0:
        return 1
    if s == 0:
        return getStone(1,i-1)
    elif len(str(s)) % 2 == 0:
        s = str(s)
        return getStone(int('0'+s[:len(s)//2]),i-1) + getStone(int('0'+s[len(s)//2:]),i-1)
    else:
        return getStone(s*2024,i-1)


for s in stones:
    ans += getStone(s,75)
    # ans += len(stones_final)
    # print(stones_final[:10])

# print(stones)
# ans = len(stones)
# print(a)

print(f'ans:{ans}')
