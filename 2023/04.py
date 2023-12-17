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
import re
r=re.compile(r'(\d+)')
copies=[1 for _ in rl(lines)]
for i, l in enumerate(lines):
    l=l.split(': ')[1]
    l=l.split(' | ')
    w=r.findall(l[0])
    c=r.findall(l[1])
    cs=0
    d=1
    for card in c:
        if card in w:
            if cs:cs*=2
            else:cs=1
            if p == 2:
                copies[i+d]+=copies[i]
                d+=1
    if p == 1: ans+=cs
if p == 2: ans = sum(copies)
## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
