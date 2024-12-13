#!/bin/python3
import sys, re
from collections import deque
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]


ans = 0

a = ints(lines[0])[0]
b = ints(lines[1])[0]
c = ints(lines[2])[0]

program = ints(lines[-1])

print(a, b, c, program)

ip=0

out=[]

# if not test: exit()

while ip < len(program):
    i=program[ip]
    cb=program[ip+1]
    lop=cb

    assert cb != 7

    if cb > 3:
        if cb == 4: cb = a
        elif cb == 5: cb = b
        elif cb == 6: cb = c

    if i == 0:
        a = a // 2**cb
    if i == 1:
        b ^= lop
    if i == 2:
        b = cb&0b111
    if i == 3:
        if a != 0: ip = lop - 2
    if i == 4:
        b ^= c
    if i == 5:
        out += [cb%8]
    if i == 6:
        b = a // 2**cb
    if i == 7:
        c = a // 2**cb
    
    ip += 2

ans = ','.join(list(map(str, out)))

print(f'ans:{ans}')
