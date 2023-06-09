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
ans = 'No answer calculated yet'

def snafuParse(snum):
    snum = snum[::-1]
    place = 1
    num = 0
    for part in snum:
        if part == '=':
            num += place * -2
        elif part == '-':
            num += place * -1
        else:
            num += place * int(part)
        place *= 5
    return num


## snafuParse(snafuMake(31415)) == 31415

def to_snafu(num):
    """5space's code I stolen"""
    if num in range(-2, 3):
        return "012=-"[num]
    else:
        return to_snafu(round(num / 5)) + "012=-"[num % 5]

def to_snafu(num):
    """my own spin off his recursive solution
    this still doesn't count tho"""
    snafu = ''
    while num > 0:
        snafu = "012=-"[num % 5] + snafu
        num = round(num / 5)
    return snafu

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
print(snafuParse("1121-1110-1=0"))
print(snafuParse("1=0"))

nums = lm(snafuParse, lines)
s = sum(nums)
print(numberToBase(s, 2))
ans = to_snafu(sum(nums))

## your code goes here
if p == 1:
    # ans = 1337
    pass
else: ## part 2
    # ans = 13371337
    pass

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
