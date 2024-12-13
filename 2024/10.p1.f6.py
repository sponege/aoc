#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
inp=inp.strip()
print('read everything')

ans = 0

g = [[int(c) for c in l] for l in lines]
if test: print(g)

h=len(g)
w=len(g[0])

d2=[[0,1],[0,-1],[1,0],[-1,0]]

def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

for x in range(w):
    for y in range(h):
        if g[y][x] != 0: continue
        # print('start',x,y)
        # print(x,y)
        cs=0
        ps=[(x,y)]
        # print(ps)
        seen=set()
        # for cx,cy in ps:
        while len(ps):
            cx,cy=ps.pop()
            # print(g[cy][cx],cx,cy)
            if (cx,cy) in seen: continue
            if g[cy][cx] == 9: cs += 1
            seen.add((cx,cy))
            # print(cx,cy,g[cy][cx])

            for dx,dy in d2:
                nx,ny=cx+dx,cy+dy
                if check(nx,ny) and g[ny][nx]-1==g[cy][cx]:
                    # if g[ny][nx] == 9: cs += 1
                    ps.append((nx,ny))
        ans += cs
        if cs: print(x, y, cs)
        # print(seen)


# for l in lines:
#     ins, op1, op2, op3 = l.split()

print(f'ans:{ans}')
