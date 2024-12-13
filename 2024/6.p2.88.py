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

sx,sy=findLetter('^', lines)

for wx in range(w):
    for wy in range(h):
        if wx == sx and wy == sy: continue
        x=sx
        y=sy
        dc=0
        s=set()
        while 1:
            dx,dy=ds[dc]
            nx,ny=(dx+x,dy+y)
            if not check(nx,ny): break
            if g[ny][nx] == '#' or (ny == wy and nx == wx):
                dc+=1
                dc%=4
            else:
                if (nx,ny,dc) in s:
                    # print(wx,wy,(x,y,dc))
                    ans += 1
                    break
                x,y=(nx,ny)
            
            s.add((x,y,dc))


# ans=len(s)
# ans+=1
# print(s)
print(f'ans:{ans}')