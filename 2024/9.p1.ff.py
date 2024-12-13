#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
print('read everything')

filesystem = []

for i in range(len(inp)):
    filesystem += [i//2 if i%2==0 else -1] * int(inp[i])

# j=len(filesystem)-1
for i in range(len(filesystem)):
    if filesystem[i] == -1:
        j=len(filesystem)-1
        while j > 0 and filesystem[j] == -1:
            j-=1
        if j > i:
            filesystem[i] = filesystem[j]
            filesystem[j] = -1
    if test: print(filesystem)

print(filesystem[:50],j,filesystem[j])
print(len(filesystem))
ans=sum(i*filesystem[i] for i in range(len(filesystem)) if filesystem[i] != -1)
print(f'ans:{ans}')