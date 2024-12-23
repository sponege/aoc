#!/bin/python3

# this video is sponsored by taco bell

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=0

a=6 if test else 70
w=a
h=a

inp=inp.strip()
print('read everything')

bytes = set() # keyword? womp womp

g = {}

for l in lines[:12 if test else 1024]:
    x,y = ints(l)
    bytes.add((x,y))
    g[(x,y)] = '#'

# for x,y in list(bytes):
    # if (x,y+1) not in bytes: g[(x,y+1)] = '#'


# w = 101
# h = 103
# ans=0
if test: print_board(g)


from collections import deque

d2=[[0,1],[-1,0],[0,-1],[1,0]]
def check(x,y):
    return x >= 0 and x <= w and y >= 0 and y <= h and (x,y) not in g

visited = {}

paths=deque([[0,0,0]])
while paths:
    cx,cy,s = paths.popleft()
    # print(cx,cy,s,w,h)
    if (cx,cy) in visited and s >= visited[(cx,cy)]: continue
    else: visited[(cx,cy)] = s
        
    if cx == w and cy == h:
        ans = s
        break
    for dx,dy in d2:
        nx,ny=cx+dx,cy+dy
        if check(nx,ny):
            paths.append([nx,ny,s+1])


print(f'ans:{ans}')
