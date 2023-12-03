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
ans = 0 
import re

if p == 1:
    lines = [list(l+'.') for l in lines]
    r=re.compile('(\d+)!')
    for x in rl(lines[0]):
        for y in rl(lines):
            if lines[y][x] in '0123456789.!':continue
            lines[y][x]='!'
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    cx,cy=(dx+x,dy+y)
                    try:
                        if lines[cy][cx] in '0123456789':
                            while True:
                                cx+=1
                                if cx>=len(lines[0]):break
                                if lines[cy][cx] in '!.':
                                    lines[cy][cx]='!'
                                    break
                    except:pass

    for l in lines:
        l=''.join(l)
        a=r.findall(l)
        print(l)
        for b in a:
            ans+=int(b)
    
if p == 2:
    lines = [list(l+'.') for l in lines]
    r=re.compile('(\d+)!')
    for x in rl(lines[0]):
        for y in rl(lines):
            if lines[y][x]!='*':continue 
            nums=[]
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    cx,cy=(dx+x,dy+y)
                    try:
                        if lines[cy][cx] in '0123456789':
                            # read number
                            while cx>=0 and lines[cy][cx] in '0123456789':cx-=1
                            cx+=1
                            num=''
                            while cx<len(lines[0]) and lines[cy][cx] in '0123456789':
                                num+=lines[cy][cx]
                                cx+=1
                            num=int(num)
                            print(num)
                            if num in nums:continue
                            nums.append(num)
                    except:pass
            print(nums)
            if len(nums)==2:ans+=nums[0]*nums[1]

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
