#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

ans = 0

boxes=[]
for _ in range(256):boxes.append({})

if p == 1:
    for thing in lines[0].split(','):
        cur=0
        for c in thing:
            cur+=ord(c)
            cur*=17
            cur%=256
        ans += cur

if p == 2:
    for thing in lines[0].split(','):
        if '=' in thing:
            lens,num = thing.split('=')
            num=int(num)
        if '-' in thing:
            lens=thing.split('-')[0]
        cur=0
        for c in lens:
            cur+=ord(c)
            cur*=17
            cur%=256
        
        if '=' in thing:
            boxes[cur][lens] = num
        else:
            if lens in boxes[cur]: del boxes[cur][lens]


    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            ans += (i+1) * (j+1) * box[lens]

## submit answer you got to the utils function
final(t, p, ans, expected_ans)