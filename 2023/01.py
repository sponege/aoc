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

if p == 1:
    f=inp
    for l in lines:
        n=''
        for a in l:
            if a in '0123456789':
                n+=a
                break
        for a in l[::-1]:
            if a in '0123456789':
                n+=a
                break

        n=int(n)
        ans+=n

if p == 2:
    for l in lines:
        n=''
        a=l
        while True:
            done=False

            s=['zero','one','two','three','four','five','six','seven','eight','nine']
            for thing in s:
                if a[:len(thing)] == thing:
                    n+=str(s.index(thing))
                    done=True
                    break
            if done: break
            s='0123456789'
            for thing in s:
                if a[:len(thing)] == thing:
                    n+=str(s.index(thing))
                    done=True
                    break
            if done:break
            a=a[1:]
        if not done: real_print('oof', l)
        a=l
        while True:
            done=False
            s=['zero','one','two','three','four','five','six','seven','eight','nine']
            for thing in s:
                if a[-len(thing):] == thing:
                    n+=str(s.index(thing))
                    done=True
                    break
            if done: break
            s='0123456789'
            for thing in s:
                if a[-len(thing):] == thing:
                    n+=str(s.index(thing))
                    done=True
                    break
            if done: break
            a=a[:-1]

        n=int(n)
        print(n)
        ans+=n

    # ans = 13371337
    pass

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
