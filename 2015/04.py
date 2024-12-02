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

inp=inp.strip()
# md5 hashing
import hashlib
ans=0
## your code goes here
if p == 1:
    # ans = 1337
    while True:
        ans+=1
        if hashlib.md5((inp+str(ans)).encode()).hexdigest()[0:5] == '00000':
            print(hashlib.md5((inp+str(ans)).encode()).hexdigest())
            break
    pass
else: ## part 2
    # ans = 13371337
    while True:
        ans+=1
        if hashlib.md5((inp+str(ans)).encode()).hexdigest()[0:6] == '000000':
            print(hashlib.md5((inp+str(ans)).encode()).hexdigest())
            break

    pass

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
