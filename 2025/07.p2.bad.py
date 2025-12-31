import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0


g = [list(l) for l in lines]
def find(c):
    for y in range(len(g)):
        if c in g[y]: return (g[y].index(c), y)
def get(x,y):
    if x < 0 or x >= len(g[0]) or y < 0 or y >= len(g): return '!'
    else: return g[y][x]
# if not test: exit()

sx, sy = find('S')
ps=[[sx,sy]]

seen=set()
while ps:
    x,y = ps.pop()
    # print(x,y,get(x,y))
    k = (x,y)
    if k in seen: continue

    seen.add(k)

    y += 1

    if get(x,y) == '!': continue
    if get(x,y) == '^':
        ps.append([x-1,y])
        ps.append([x+1,y])
        ans += 1
    else:
        ps.append([x,y])
    # print(ps)

# print(ps)
print(f'ans:{ans}')