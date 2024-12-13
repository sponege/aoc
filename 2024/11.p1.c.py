#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
pp = lambda *args: [print(*args) if test else 0]

inp=inp.strip()
# print('read everything')

stones = list(map(int, inp.split()))

i=0
while i < 25:
    ns=[]
    for s in stones:
        if s == 0: ns += [1]
        elif len(str(s)) % 2 == 0:
            s = str(s)
            ns += [int('0'+s[:len(s)//2]), int('0'+s[len(s)//2:])]
        else:
            ns += [s*2024]
    stones=ns
    i += 1

# print(stones)
ans = len(stones)

print(f'ans:{ans}')
