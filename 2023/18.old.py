#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

import re
r=re.compile(r'(\d+)')
ans = 0

grid={}

x,y=(0,0)
grid[(x,y)]='#'
sx,sy=(0,0)
j=2
for l in lines:
    dir, steps, color = l.split(' ')
    dx,dy = [[0,-1],[0,1],[1,0],[-1,0]]["UDRL".index(dir)]
    steps=int(steps)

    if p == 2:
        print(color[7], color[2:7])
        steps = int(color[2:7], 16)
        dx,dy = [[0,-1],[0,1],[1,0],[-1,0]]["3102".index(color[7])]

    for i in range(steps):
        x+=dx
        y+=dy
        grid[(x,y)]='#'
    if j>0:
        sx+=dx
        sy+=dy
        j-=1
print(sx,sy)

paths=[(sx,sy)]

while len(paths)>0:
    nps=[]
    for x,y in paths:
        for dx,dy in [[0,-1],[0,1],[1,0],[-1,0]]:
            nx,ny=(x+dx,y+dy)
            if (nx,ny) in grid: continue
            grid[(nx,ny)]='#'
            nps.append((nx,ny))
    paths=nps

ans = len(grid.keys())

# print_board(grid)
## submit answer you got to the utils function
final(t, p, ans, expected_ans)