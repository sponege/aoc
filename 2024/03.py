#!/bin/python3

import sys, re
from util import *

p, d, t, inp, lines = getArgs()
print('read everything')

ans = 0

do = 1

while inp:
    if inp[:4]=='do()':do=1
    if inp[:7]=="don't()":do=0
    if inp[:4] == 'mul(':
        t=inp.split(')')[0].split('(')[1]
        if ',' in t:
            t=t.split(',')
            ot=t
            t=[''.join([a for a in b if a in '0123456789']) for b in t]
            if t == ot: 
                #print(t)
                a,b = map(int,t)
                if do:ans+=a*b
    inp=inp[1:]

print(f'ans:{ans}')

