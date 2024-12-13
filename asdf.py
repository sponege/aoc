#!/bin/python3

import sys, re
from util import *

p, d, t, inp, lines = getArgs()

ans = 0

t=inp.split(', ')
x=0
y=0

for a in t:
    d,i=a[0],a[1:]
    i=int(i)
    if d == 'L':x-=i
    if d == 'R':x+=i
    if d == 'U':y+=i 
    if d == 'D':y-=i

ans=abs(y)+abs(x)

print(f'ans:{ans}')

