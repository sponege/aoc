#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
print('read everything')

ans = 0

ins=inp.split(', ')
x=0
y=0

ds=[[0,1],[1,0],[0,-1],[-1,0]]
ls=set()
d=0
c=1
for i in ins:
    c,n=i[0],i[1:]
    n=int(n)
    if c == 'L':d+=1
    if c == 'R':d-=1
    d%=4
    dx,dy=ds[d]
    
    for _ in range(n):
        y+=dy;
        x+=dx;
        if (x,y) in ls:
            print(x,y)
            c=0

            break
        ls.add((x,y))
    if not c:break


ans=abs(x)+abs(y)
print('test?', test)

print(f'ans:{ans}')

