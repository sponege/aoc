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
ans = 'No answer calculated yet'

countVowels = lambda s: len([c for c in s if c in 'aeiou'])

## your code goes here
if p == 1:
    # ans = 1337
    strings = [countVowels(s) >= 3 and re.search(r'([a-z])\1', s) and not re.search(r'ab|cd|pq|xy', s) for s in lines]
    ans = strings.count(True)
    pass
else: ## part 2
    # ans = 13371337
    strings = [re.search(r'([a-z]{2}).*\1', s) and re.search(r'([a-z]).\1', s) for s in lines]
    ans = len(strings) - strings.count(None)
    pass

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
