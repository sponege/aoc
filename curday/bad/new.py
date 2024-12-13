#!/bin/python3

import sys, re
from util import *


p, d, t, inp, lines = getArgs()

cl=0
ans = 0
for l in lines:
    s=1
    l=list(map(int, l.split()))
    ol=list(l)
    for j in range(len(l)):
        l=[i for k,i in enumerate(ol) if j!=k]
        s=1
        t=l[0]>l[1]
        for i in range(len(l)-1):
             if int(l[i]>l[i+1]) != int(t):
                 s=1
             if abs(l[i]-l[i+1])>3 or abs(l[i]-l[i+1])<1:
                 s=1
        if not s:
            break

    if s: ans += 1
    #else: print(l)
    cl+=1

print('skibidi')
print(f'ans:{ans}')

