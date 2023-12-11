#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

## you don't want to print a lot of debug info if you aren't in debug mode!
real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

ans = 0

grid={}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '#': grid[(x,y)]='#'

x=0
times_larger=1000000-1 if p == 2 else 2-1
while True:
    if len([p[0] for p in grid.keys() if p[0] == x]) == 0:
        for px, py in grid.copy().keys():
            if px>x:
                del grid[(px,py)]
                grid[(px+times_larger,py)]='#'
        x+=times_larger
    x+=1
    minx, maxx = min_max([x for x, _ in grid])
    miny, maxy = min_max([y for _, y in grid])
    if x>maxx:break

y=0
while True:
    if len([p[1] for p in grid.keys() if p[1] == y]) == 0:
        for px, py in grid.copy().keys():
            if py>y:
                del grid[(px,py)]
                grid[(px,py+times_larger)]='#'
        y+=times_larger
    y+=1
    minx, maxx = min_max([x for x, _ in grid])
    miny, maxy = min_max([y for _, y in grid])
    if y>maxy:break
# print_board(grid)

pts=[]
for x, y in grid.keys():
    pts.append({'x': x, 'y': y})

for i, p1 in e(pts):
    for p2 in pts[i:]:
        d = abs(p1['x']-p2['x']) + abs(p1['y']-p2['y'])
        ans += d

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
