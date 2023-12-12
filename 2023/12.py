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
r=re.compile(r'(#+)')
ans = 0

_=0
for line in lines:
    _+=1
    print("line", _)
    row, groups = line.split(' ')
    groups = [int(i) for i in groups.split(',')]
    print(line)
    one = 0
    two = 0
    # if p == 2: row = '?' + row
    for i in range(2**row.count('?')):
        nr = list(row)
        k = 0
        for j, c in enumerate(nr):
            if c == '?':
                nr[j] = '#' if (i>>k)&1 else '.'
                k += 1
        # print(nr, r.findall(''.join(nr)))
        if [len(a) for a in r.findall(''.join(nr))] == groups:
            if p == 1: ans += 1
            one += 1
    if p == 2: # non-working solution for part 2, works on test input
        row = ('?' if row[-1] != '#' else '.') + row + ('?' if row[0] != '#' else '.')
        for i in range(2**row.count('?')):
            if row[-1] == '#': 
                two = one
                break
            nr = list(row)
            k = 0
            for j, c in enumerate(nr):
                if c == '?':
                    nr[j] = '#' if (i>>k)&1 else '.'
                    k += 1
            # print(nr, r.findall(''.join(nr)))
            if [len(a) for a in r.findall(''.join(nr))] == groups:
                # ans += 1
                two += 1
        ans += one*two*two*two*two
        print(one*two*two*two*two)
    # break
        

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
