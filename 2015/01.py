#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

## you don't want to print a lot of debug info if you aren't in debug mode!
if not d:
    real_print = print
    print = lambda *args, **kwargs: None

# some helpful information:
# the variable p stores what part you are currently on, it's either 1 or 2
# make your script work with both parts by using if p == 1: ... else: ...
# the variable d is a boolean; it returns if you are in debug mode or not
# the submit function works 
# the variable t is a boolean; it returns if you are in test mode or not

## your code goes here
if p == 1:
    ans = inp.count('(') - inp.count(')')
else:
    ans = 0
    floor = 0
    for c in inp:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        ans += 1
        if floor == -1:
            break
## restore print
if not d:
    print = real_print

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
