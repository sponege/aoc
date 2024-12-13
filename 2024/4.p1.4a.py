#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
import sys
lines = sys.stdin.read().splitlines()

ans = 0

g = [list(l) for l in lines]

w=len(g[0])
h=len(g)

def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

for sx in range(w):
    for sy in range(h):
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                c=g[sy][sx]
                cx=sx
                cy=sy
                i=1
                while check(cx,cy) and i < 4:
                    cx+=dx
                    cy+=dy
                    if not check(cx,cy) and i < 4:break
                    c+=g[cy][cx]
                    i+=1
                if c[:4] == 'XMAS': ans += 1
print(ans)

print(f'ans:{ans}')

