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
for l in lines:
    dir, steps, color = l.split(' ')
    dx,dy = [[0,-1],[0,1],[1,0],[-1,0]]["UDRL".index(dir)]
    steps=int(steps)

    if p == 2:
        print(color[7], color[2:7])
        steps = int(color[2:7], 16)
        dx,dy = [[0,-1],[0,1],[1,0],[-1,0]]["3102".index(color[7])]
    x+=dx*steps
    y+=dy*steps
    grid[(x,y)]='#'

def get_area(loop):
    # thanks 5space for the code again....
    double_area = abs(sum(x0*y1 - x1*y0 for (x0, y0), (x1, y1) in zip(loop, loop[1:] + [loop[0]])))
    boundary = sum(abs(x0 - x1) + abs(y0 - y1) for (x0, y0), (x1, y1) in zip(loop, loop[1:] + [loop[0]]))
    return (double_area - boundary) // 2 + 1 + boundary

ans = get_area(list(grid.keys()))

# print_board(grid)
## submit answer you got to the utils function
final(t, p, ans, expected_ans)