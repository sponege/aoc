#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
pp = lambda *args: [print(*args) if test else 0]

ans=0

inp=inp.strip().split('\n\n')
print('read everything')

from collections import deque

for t in inp:
    a,b,p = t.split('\n')
    o = []
    for b in [a,b]:
        b = b.split(': ')[1].split(', ')
        xp = int(b[0].split('+')[1])
        yp = int(b[1].split('+')[1])
        o += [[xp,yp]]
    px, py = p.split(', ')
    px = int(px.split('=')[1])
    py = int(py.split('=')[1])
    if test: print(o, px, py)
    ps = deque([[0,0,0,0]])
    # while ps:
    #     print(len(ps))
    #     x,y,As,Bs=ps.popleft()

    #     if As > 100 or Bs > 100: continue
    for As in range(101):
        for Bs in range(101):
            x = o[0][0] * As
            x += o[1][0] * Bs
            y = o[0][1] * As
            y += o[1][1] * Bs

            if x == px and y == py:
                ans += 3*As + Bs
                break

        # ps.append([x+o[0][0],y+o[0][1],As+1,Bs])
        # ps.append([x+o[1][0],y+o[1][1],As,Bs+1])



print(f'ans:{ans}')
