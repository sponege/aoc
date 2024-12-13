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

robots=[]
for l in inp.split('\n'):
    a,b = l.split(' v=')
    a=a.split('=')[1]
    a = list(map(int, a.split(',')))
    b = list(map(int, b.split(',')))
    sx,sy = a
    vx,vy = b
    c = 101
    d = 103
    if 0:
        c = 11
        d = 7
    robots.append((sx,sy,vx,vy))
w = 101
h = 103
ans=0
d2=[[0,1],[-1,0],[0,-1],[1,0]]
def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

def get(x,y,g):
    if check(x,y): return g[y][x]
    else: return 0

# gg thanks for watching

for i in range(10000000):
    if i % 20 == 0: print(i)
    fail=0
    g = [[0 for _ in range(w)] for _ in range(h)]
    for sx,sy,vx,vy in robots:
        fx = (sx + (vx*i)) % c
        fy = (sy + (vy*i)) % d
        if g[fy][fx]: g[fy][fx] = 7; fail = 1; break
        g[fy][fx] = 1
    if not fail:
        for y in range(h):
            for x in range(w):
                print('#' if g[y][x] else ' ', end='')
            print()
    # for x in range(w):
    #     for y in range(h):
    #         f=1
    #         # for dx,dy in d2:
    #         #     nx,ny=x+dx,y+dy
    #         #     if check(nx,ny) and g[ny][nx] == 1:
    #         #         f=0
    #         #         break
    #         if f: fail=1; break
    #     if fail: break
    if not fail:
        ans=i
        break


print(f'ans:{ans}')
