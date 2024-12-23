#!/bin/python3

# this video is sponsored by taco bell

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=0

a=6 if test else 70
w=a+1
h=a+1

# if not test: exit()
inp=inp.strip()
print('read everything')

bytes = set() # keyword? womp womp

g = {}

for i in range(1000000):
    x,y = ints(lines[i])
    bytes.add((x,y))
    g[(x,y)] = '#'

    # for x,y in list(bytes):
        # if (x,y+1) not in bytes: g[(x,y+1)] = '#'


    # w = 101
    # h = 103
    ans='bruh'
    d2=[[0,1],[-1,0],[0,-1],[1,0]]
    def check(x,y):
        return x >= 0 and x < w and y >= 0 and y < h and (x,y) not in g

    dp={}
    from collections import deque
    ps=deque([[0,0,0]])
    while ps:
        cx,cy,s = ps.popleft()
        # print(cx,cy,s,w,h)
        if (cx,cy) in dp and s >= dp[(cx,cy)]: continue
        else: dp[(cx,cy)] = s
            
        if cx == w-1 and cy == h-1:
            ans = s
            break
        for dx,dy in d2:
            nx,ny=dx+cx,dy+cy
            if check(nx,ny):
                ps.append([nx,ny,s+1])
    if ans == 'bruh':
        ans = lines[i]
        break
print_board(g)


print(f'ans:{ans}')
