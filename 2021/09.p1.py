#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
inp=inp.strip()
print('read everything')

ans = 0

g = [[int(c) for c in l] for l in lines]

h=len(g)
w=len(g[0])

d2=[[0,1],[0,-1],[1,0],[-1,0]]

def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

for x in range(w):
    for y in range(h):
        lowest=1
        for dx,dy in d2:
            nx,ny=x+dx,y+dy
            if not check(nx,ny): continue
            if not (g[y][x] < g[ny][nx]): lowest = 0; break
        if lowest:
            print(x,y)
            ans += 1 + g[y][x]

print(f'ans:{ans}')