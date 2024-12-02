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

def extract(s):
    ns=[]
    for i in range(len(s)-1):
        ns.append(s[i+1]-s[i])
    return ns

for l in lines:
    sequences=[[int(i) for i in r.findall(l)]]
    while True:
        next=extract(sequences[-1])
        sequences.append(next)
        if len([n for n in next if n == 0]) == len(next): break
    print(sequences)
    if p == 1: ans += sum(s[-1] for s in sequences)
    if p == 2:
        c=sequences[-1][0]
        for i in range(len(sequences)-1,-1,-1):
            c=sequences[i][0]-c
        print(c)
        ans+=c

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
