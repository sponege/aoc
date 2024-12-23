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

g=g\
.replace('#','##')\
.replace('O','[]')\
.replace('.','..')\
.replace('@','@.')

g = [l for l in g.split('\n')]
w=len(g[0])
h=len(g)

ds = list(filter(lambda c: c in 'v>^<', ds))


x,y = findLetter('@', g)

g = [list(l) for l in g]
g[y][x] = '@'
print('\n'.join(''.join(l) for l in g)+'\n')
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
    oy,ox=y,x
    g[y][x] = '!'
    a=0
    reaches = []
    last_reaches=[x]
    # while g[cy][cx] not in '.#':
    UHH_WALL = 0
    while not all(g[cy+dy][xx] in '.'+('[]'if dx else '') for xx in last_reaches) and check(cx,cy):
        # print(len(reaches), cx, cy)
        if test: print(last_reaches)
        if test:
            # print(cy, last_reaches)
            # print(d)
            # print('\n'.join(''.join(l) for l in g)+'\n')
            pass
        cx += dx
        cy += dy
        cur_reaches = set()
        for xx in last_reaches:
            while g[cy][xx] not in '.' and check(xx,cy):
                # print('oh NO', len(last_reaches), xx, cy, check(xx,cy))
                xx += dx
                if g[cy][xx] == '#':
                    UHH_WALL = 1
                    break
                if g[cy][xx] == '[':
                    cur_reaches.add(xx)
                    cur_reaches.add(xx+1)
                elif g[cy][xx] == ']':
                    cur_reaches.add(xx-1)
                    cur_reaches.add(xx)
                if dx == 0: break
        if UHH_WALL: break
        last_reaches=list(cur_reaches)
        reaches += [last_reaches]
    g[oy][ox] = '.'
    if test: print(last_reaches, UHH_WALL)
    # if test:print(a)
    # if g[cy][cx] == '.':
    if not UHH_WALL:
        # print('gottem', len(reaches))
        o=None
        # if test: print('wow!', cy, cx, y, x)
        # while not (cy == y and cx == x):
        #     ox = cx
        #     oy = cy
        #     cx -= dx
        #     cy -= dy
        #     g[oy][ox] = g[cy][cx]
        if test: print('reaches', reaches)
        for i in range(len(reaches)):
            for xx in sorted(reaches[-i-1], reverse=d=='>'):
                # g[cy+dy][x+dx] = g[cy][x]
                if test: print(cy, cx, i, dy, dx, xx)
                # g[cy-i][x] = g[cy+dy][x+(dx*2)]
                # g[cy+dy][x+(dx*2)] = g[cy-i][x]
                
                g[cy+(dy)][xx+(dx)] = g[cy][xx]
                g[cy][xx] = '.'
            # if test: print(oy, ox, cy, cx, g[oy][ox], g[cy][cx])
        # g[y][x] = '.'
            if test: print(f'{i=}')
            if i != len(reaches) - 1:
                cx -= dx
                cy -= dy
        x += dx
        y += dy
        # x += dx
        # y += dy*2
    # else: g[y][x] = '.'

    g[y][x] = '@'
    if test: print(d)
    if test: print('\n'.join(''.join(l) for l in g)+'\n')

    g[y][x] = '.'
g[y][x] = '@'
if test:
    pass
print('\n'.join(''.join(l) for l in g)+'\n')

ans = 0
for x in range(w):
    for y in range(h):
        if g[y][x] == '[':
            ans += (100 * y) + x

print(len(ds))
print(f'ans:{ans}')
