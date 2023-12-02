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

# some helpful information:
# the variable p stores what part you are currently on, it's either 1 or 2
# make your script work with both parts by using if p == 1: ... else: ...
# the variable d is a boolean; it returns if you are in debug mode or not
# the submit function works 
# the variable t is a boolean; it returns if you are in test mode or not
ans = 0 

## your code goes here
ans_two=0
for y, l in e(lines):
    l=l.split(": ")[1]
    games=l.split("; ")
    fail=0
    rm=0
    gm=0
    bm=0
    for g in games:
        g=g.replace(' blue',' b').replace(' red',' r').replace(' green',' g')
        vals=[z.split(' ') for z in g.split(', ')]
        r=12
        g=13
        b=14
        for z in vals:
            i=int(z[0])
            if z[1]=='r':
                rm=max(i,rm)
                r-=i
            if z[1]=='g':
                gm=max(i,gm)
                g-=i
            if z[1]=='b':
                bm=max(i,bm)
                b-=i
        if not fail: fail = r < 0 or g < 0 or b < 0
    ans_two+=rm*gm*bm
    print(y+1, rm, gm,  bm)
    if not fail: ans+=y+1
if p == 2:
    ans=ans_two
## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
