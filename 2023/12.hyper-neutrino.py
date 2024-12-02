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

cache = {}

def count(row, groups):
    if row == '':
        return 1 if groups == () else 0
    
    if groups == ():
        return 0 if "#" in row else 1

    key = (row, groups)

    if key in cache:
        return cache[key]
       
    result = 0

    if row[0] in '.?':
        result += count(row[1:], groups)
    
    if row[0] in '#?':
        if groups[0] <= len(row) and '.' not in row[:groups[0]] and (groups[0] == len(row) or row[groups[0]] != '#'):
            result += count(row[groups[0] + 1:], groups[1:])

    cache[key] = result
    return result    

for line in lines:
    row, groups = line.split(' ')
    groups = tuple(map(int, groups.split(',')))

    if p == 2:
        row = '?'.join([row] * 5)
        groups *= 5

    ans += count(row, groups)

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
