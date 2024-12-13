#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
print('read everything')
g = [list(l) for l in lines]
ans = 0
w=len(g[0])
h=len(g)

g = [list(l) for l in lines]
ds=[[0,-1],[1,0],[0,1],[-1,0]]
dsm='^>v<>'
dc=0

def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

s=set()
x,y=findLetter('^', lines)

from collections import deque
ps=deque([[x,y,s,0,0]])

real=set()

while ps:
    # print('a',len(ps))
    x,y,s,ok,checkloop=ps.popleft()
    dx,dy=ds[dc]
    nx,ny=(dx+x,dy+y)
    if not check(nx,ny): break
    if (x,y) in s and not ok:
        # ans += 1
        # print((nx,ny))
        real.add((x,y))
        continue
    if g[ny][nx] == '#' and (nx,ny) not in s:
        dc+=1
        dc%=4
    else:
        # if (nx,ny) in s: ans += 1; print(nx,ny)
        # s.add((x,y))
        ps.append([nx,ny,s|set(),0,checkloop])
        if not len(s) or 0: ps.append([x,y,s|set({(x,y)}),1,1])
        x,y=(nx,ny)


# ans=len(s)
# ans+=1
# print(s)
ans=len(real)
print(real)
print(f'ans:{ans}')