#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
print('read everything')
g = [list(l) for l in lines]
ans = 0
# w=len(g[0])
# h=len(g)

g = [list(l) for l in lines]
ds=[[0,-1],[1,0],[0,1],[-1,0]]
dsm='^>v<>'
dc=0

from collections import defaultdict
nodes=defaultdict(list)

w=len(g[0])
h=len(g)

def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h # and g[y][x] in '.'

antinodes=set()

for x in range(w):
    for y in range(h):
        if g[y][x] not in './':
            for otherx, othery in nodes[g[y][x]]:
                odiffx, odiffy = x - otherx, y - othery
                for i in range(0,10000):
                    diffx = odiffx * i
                    diffy = odiffy * i
                    if check(x + diffx, y + diffy):
                        # g[y + diffy][x + diffx] = '/'
                        antinodes.add((x + diffx, y + diffy))
                    if check(otherx - diffx, othery - diffy): 
                        # g[othery - diffy][otherx - diffx] = '/'
                        antinodes.add((otherx - diffx, othery - diffy))
                    if check(x + diffx, y + diffy):
                        # g[y + diffy][x + diffx] = '/'
                        antinodes.add((x + diffx, y + diffy))
                    if check(otherx - diffx, othery - diffy): 
                        # g[othery - diffy][otherx - diffx] = '/'
                        antinodes.add((otherx - diffx, othery - diffy))
            nodes[g[y][x]] += [(x,y)]
# ans = sum(l.count('/') for l in g)
for x, y in antinodes:
    g[y][x] = '/'
ans = len(antinodes)
print('\n'.join(''.join(l) for l in g))

# chonky keyboard very cool
print(f'ans:{ans}')