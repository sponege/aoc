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

from math import lcm
ans = 0

nodes={}
path=lines[0]

for node in lines[2:]:
    nodes[node[:3]] = (node[7:10], node[12:15])
print(nodes)

if p == 1:
    steps=0
    cur='AAA'
    pathcur=0
    while cur != 'ZZZ':
        cur = nodes[cur][0 if path[pathcur] == 'L' else 1]
        pathcur+=1
        pathcur%=len(path)
        steps+=1
    ans = steps

if p == 2:
    steps=0
    ghosts=[node for node in nodes.keys() if node[-1] == 'A']
    pathcur=0
    steps_all=[]
    for i, ghost in e(ghosts):
        steps=0
        while True:
            ghosts[i] = nodes[ghosts[i]][0 if path[pathcur] == 'L' else 1]
            pathcur+=1
            pathcur%=len(path)
            steps+=1
            if ghosts[i][-1] == 'Z': break
        steps_all.append(steps)
    print(steps_all)
    ans = lcm(*steps_all)

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
