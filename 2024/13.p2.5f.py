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
    wow = 10000000000000
    # wow = 0
    px = int(px.split('=')[1]) + wow
    py = int(py.split('=')[1]) + wow
    if test: print(o, px, py)
    ps = deque([[0,0,0,0]])
    # while ps:
    #     print(len(ps))
    #     x,y,As,Bs=ps.popleft()

    #     if As > 100 or Bs > 100: continue
    # for As in range(10001):
    #     for Bs in range(10001):
    #         x = o[0][0] * As
    #         x += o[1][0] * Bs
    #         y = o[0][1] * As
    #         y += o[1][1] * Bs

    #         if x == px and y == py:
    #             ans += 3*As + Bs
    #             break
    a = o[0][0]
    b = o[1][0]
    c = px
    d = o[0][1]
    e = o[1][1]
    f = py
    As = ((c*e)-(f*b)) / \
        ((a*e)-(b*d))
    Bs = ((a*f)-(c*d)) / \
        ((a*e)-(b*d))
    if int(As) != As or int(Bs) != Bs: continue
    As = int(As)
    Bs = int(Bs)
    # if As > 100 or Bs > 100: continue
    ans += 3*int(As) + int(Bs)
    if test:
        print(px, py, As, Bs)

        # ps.append([x+o[0][0],y+o[0][1],As+1,Bs])
        # ps.append([x+o[1][0],y+o[1][1],As,Bs+1])



print(f'ans:{ans}')
