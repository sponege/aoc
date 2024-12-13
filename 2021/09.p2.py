#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
inp=inp.strip()
print('read everything')

ans = 0

g = [[int(c) for c in l] for l in lines]

h=len(g)
w=len(g[0])

d2=[[0,1],[0,-1],[1,0],[-1,0]]

def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

basins=[]

for x in range(w):
    for y in range(h):
        lowest=1
        for dx,dy in d2:
            nx,ny=x+dx,y+dy
            if not check(nx,ny): continue
            if not (g[y][x] < g[ny][nx]): lowest = 0; break
        if lowest:
            ps=[(x+dx,y+dy) for dx,dy in d2]
            seen=set({(x,y)})
            basin=set({(x,y)})
            while len(ps):
                nx,ny=ps.pop()
                if not check(nx,ny): continue
                if g[ny][nx] == 9: continue
                cont=0
                basin.add((nx,ny))
                for dx,dy in d2:
                    nnx,nny=nx+dx,ny+dy
                    if not check(nnx,nny): continue
                    if not (g[ny][nx] < g[nny][nnx]) and (nnx,nny) not in seen: cont=1;break
                    
                    # seen.add((nnx,nny))
                if cont: continue
                seen.add((nx,ny))
                for dx,dy in d2:
                    nnx,nny=nx+dx,ny+dy
                    if not (nnx,nny) in seen: ps.append((nnx,nny))
            # print(x,y)
            # ans += 1 + g[y][x]
            # if test: print(seen)
            if 1:
                a={}
                for x,y in basin:
                    a[(x,y)]=g[y][x]
                print_board(a)
            basins.append(len(basin))

basins.sort(reverse=1)

print(basins)

ans = basins[0] * basins[1] * basins[2]

print(f'ans:{ans}')
