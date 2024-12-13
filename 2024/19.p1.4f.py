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

for towel in lines:
    ps = deque([towel])
    dp={}
    while ps:
        ct = ps.pop()
        if len(ct) in dp: continue
        else: dp[len(ct)] = 3
        # print(ct, 'ct')
        if len(ct) == 0:
            ans += 1
            break
        for t in towels:
            if ct.startswith(t):
                ps.append(ct[len(t):])

print(f'ans:{ans}')
