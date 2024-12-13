#!/bin/python3
import sys, re
from collections import deque
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=0

inp=inp.strip()
print('read everything')

g, ds = inp.split('\n\n')

g = [l for l in g.split('\n')]
w=len(g[0])
h=len(g)

ds = list(filter(lambda c: c in 'v>^<', ds))


x,y = findLetter('@', g)

g = [list(l) for l in g]
g[y][x] = '.'

ans=0
d2=[[0,1],[-1,0],[0,-1],[1,0]]
def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

def get(x,y,g):
    if check(x,y): return g[y][x]
    else: return 0

for d in ds:
    dx,dy = [[1,0],[0,-1],[-1,0],[0,1]]['>^<v'.index(d)]
    cx,cy = x,y
    g[y][x] = '!'
    a=0
    while g[cy][cx] not in '.#':
        cx += dx
        cy += dy
        a+=1
    # if test:print(a)
    if g[cy][cx] == '.':
        o=None
        # if test: print('wow!', cy, cx, y, x)
        while not (cy == y and cx == x):
            ox = cx
            oy = cy
            cx -= dx
            cy -= dy
            g[oy][ox] = g[cy][cx]
            # if test: print(oy, ox, cy, cx, g[oy][ox], g[cy][cx])
        g[y][x] = '.'
        x += dx
        y += dy
    else: g[y][x] = '.'

    g[y][x] = '@'
    

    if test:print('\n'.join(''.join(l) for l in g)+'\n')
    g[y][x] = '.'

ans = 0
for x in range(w):
    for y in range(h):
        if g[y][x] == 'O':
            ans += (100 * y) + x

print(len(ds))
print(f'ans:{ans}')
