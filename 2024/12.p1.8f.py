#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
pp = lambda *args: [print(*args) if test else 0]

ans=0

inp=inp.strip()
# print('read everything')

g = [[c for c in l] for l in lines]
if test: print(g)

h=len(g)
w=len(g[0])

d2=[[0,1],[0,-1],[1,0],[-1,0]]
seen=set()
def check(x,y):
    return (x,y) not in seen and x >= 0 and x < w and y >= 0 and y < h


for x in range(w):
    for y in range(h):
        if (x,y) in seen:continue
        t=g[y][x]
        ps=[(x,y)]
        c=set()
        d=[]
        while len(ps):
            cx,cy=ps.pop()
            c.add((cx,cy))
            if (cx,cy) in seen:continue
            seen|={(cx,cy)}
            for dx,dy in d2:
                nx,ny=cx+dx,cy+dy
                if check(nx,ny) and g[ny][nx] == t:
                    ps+=[(nx,ny)]
                elif (nx,ny) not in c and (nx,ny) not in ps:
                    d.append((nx,ny))
        # if test: print(c,len(d))
        if test: print(t, len(c), len(d))
        ans += len(c) * len(d)


print(f'ans:{ans}')
