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
presents = lms([splitter('x'), nm(int), tuple], lines)
if p == 1:
    wrapping_paper = lm(lambda x: 2*x[0]*x[1] + 2*x[1]*x[2] + 2*x[2]*x[0] + min(x[0]*x[1], x[1]*x[2], x[2]*x[0]), presents)
    ans = sum(wrapping_paper)
else: ## part 2
    ribbon = lm(lambda x: 2*min(x[0]+x[1], x[1]+x[2], x[2]+x[0]) + x[0]*x[1]*x[2], presents)
    ans = sum(ribbon)

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
