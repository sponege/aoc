#!/bin/python3
import sys, re
from collections import deque
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=float('inf')

inp=inp.strip()
print('read everything')
g = [l for l in lines]

w=len(g[0])
h=len(g)

x,y=findLetter('S',g)
ex,ey=findLetter('E',g)
g = [list(l) for l in g]


d2=[[0,1],[-1,0],[0,-1],[1,0]]
ds='v<^>'
def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

def get(x,y,g):
    if check(x,y): return g[y][x]
    else: return 0

# seen=set()

bestpath=0
ps=deque([[x,y,0,'>',[],set({(x,y)})]])

dp={}

a=0
while ps:
    # print(len(ps))
    cx,cy,s,ld,path,seen = ps.pop()
    if test:
        pass
        # ng=[list(l) for l in g]
        # for x,y in path:
        #     ng[y][x] = '8'
        # print('\n'.join(''.join(l) for l in ng))
    # else: exit()
    if (cx,cy) in dp and s >= dp[(cx,cy)]: continue
    else:
        dp[(cx,cy)] = s
        if a % 10000 == 0: print(dp[(cx,cy)])
    if g[cy][cx] == 'E':
        # print('WOW')
        if s < ans:
            bestpath=path
        ans = min(ans, s)
    # if test: print(cx, cy, ex, ey)
    if (cx,cy) in seen and not g[cy][cx] == 'S': continue
    seen|={(cx,cy)}
    # g[cy][cx] = '#'

    for d in range(4):# in d2:
        dx,dy=d2[d]
        nx,ny=dx+cx,dy+cy
        if check(nx,ny) and g[ny][nx] not in '#':
            ps.append([nx,ny,s+1 + (1000 if ds[d] != ld else 0),ds[d], path + [[cx,cy]], seen|{(cx,cy)}])
    a+=1
for x,y in bestpath:
    g[y][x] = '^'
print('\n'.join(''.join(l) for l in g))

print(f'ans:{ans}')
