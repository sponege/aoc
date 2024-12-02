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

import re
r=re.compile(r'(\d+)')
ans = 0
def product(l):
    p=1
    for i in l:p*=i
    return p
times=r.findall(lines[0])
distances=r.findall(lines[1])

if p == 2:
    times = [int(''.join(times))]
    distances= [int(''.join(distances))]

ways_to_win=[]
for i in range(len(times)):
    ways=0
    for s in range(int(times[i])+1):
        if (int(times[i])-s)*s > int(distances[i]): ways += 1
    ways_to_win.append(ways)
print(ways_to_win)
ans = product(ways_to_win)

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
