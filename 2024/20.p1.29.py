#!/bin/python3

# this video is sponsored by taco bell

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=0

inp=inp.strip()
print('read everything')

x,y=findLetter('S',lines)
sx,sy=x,y
ex,ey=findLetter('E',lines)

g = [list(l) for l in lines]
h = len(g)
w = len(g[0])

d2=[[0,1],[-1,0],[0,-1],[1,0]]
ds='v<^>'
def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h
dp={}

def get(x,y):
    if (x,y) in dp: return dp[(x,y)]
    else: return float('inf')

def directions(cx,cy):
    count=0
    for dx,dy in d2:
        nx,ny=cx+dx,cy+dy
        if check(nx,ny) and g[ny][nx] not in '#': count += 1
    return count
from collections import deque
# if not test: exit()
# wow=defaultdict(set)
# if not test: exit()
a=0
dp={}
def pathfind(ps):
    shortest = float('inf')
    possible = []
    c=0
    while ps:
        if c == 0: print(len(ps))
        c += 1
        c %= 10000
        cx,cy,seen,cheated,s ,path= ps.popleft()
        dp[(cx,cy)] = min(s, dp[(cx,cy)]) if (cx,cy) in dp else s
        if test:
            pass
            # ng=[list(l) for l in g]
            # for x,y in path:
            #     ng[y][x] = '8'
            # print('\n'.join(''.join(l) for l in ng))
        # else: exit()
        # ld == dp[(cx,cy)][1]
        # if (cx,cy) in dp and s > dp[(cx,cy)][0] and directions(cx,cy) < 3: continue
        # else:
        #     dp[(cx,cy)] = (s, ld)
        #     if a % 10000 == 0: print(dp[(cx,cy)])
        if g[cy][cx] == 'E':
            shortest = min(shortest, s)
            possible += [s]
        # if test: print(cx, cy, ex, ey)
        if (cx,cy) in seen and not g[cy][cx] == 'S': continue
        # seen|={(cx,cy)}
        # g[cy][cx] = '#'
        checker = 0<cheated<3
        # if g[cy][cx] == '#' and not checker: continue

        # print(cheated)
        if cheated == 0:
            ps.append([cx,cy,seen,1, s, path])
        for d in range(4):# in d2:
            dx,dy=d2[d]
            nx,ny=dx+cx,dy+cy
            if check(nx,ny) and (g[ny][nx] not in '#' or checker):
                ps.append([nx,ny,seen|{(cx,cy)},cheated+1 if checker else cheated, s+1, path+[[nx,ny]]])

    return shortest, path, possible
shortest_path, path, sp = pathfind(deque([[sx,sy,set(),3,0,[]]]))
# print(shortest_path)
# print(dp)
from collections import defaultdict

counts = defaultdict(int)

for x in range(w):
    for y in range(h):#[[3,0],[2,1],[1,2],[0,3],[-1,2],[-2,1],[-3,0]]
        for dx,dy in [[2,0],[1,1],[0,2]]:
            nx,ny=x+dx,y+dy
            a = get(x,y)
            b = get(nx,ny)
            diff = a - b
            if a == float('inf'): continue
            if b == float('inf'): continue
            diff = abs(diff)-2
            counts[diff] += 1
            if diff >= 100: ans += 1
            # print((x,y), (nx,ny))
            # if 0 < diff < 10: print(diff)
            # print(diff)
                # print((x,y), (nx,ny), a, b)
print(ans, counts)

# exit()
# _, _, possible = pathfind(deque([[sx,sy,set(),0,0,[]]]))
# print([shortest_path - ms for ms in possible])

# print(possible)
# ans = len([ms for ms in possible if shortest_path - ms == 63 ])
if test: 
    # print(path)
    i=0
    for x,y in path:
        # g[y][x] = str(i%10)
        i+=1
    # print('\n'.join(''.join(l) for l in g))
# print(wow)

# print(dp[(ex,ey)], dp[(ex+2,ey)])

print(f'ans:{ans}')
