import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()
# if test: exit()

ans = 1

boxes = []

dists = {}

connections = defaultdict(list)

for l in lines:
    x,y,z = map(int, l.split(','))
    boxes.append((x,y,z))

for i, (x,y,z) in enumerate(boxes):
    for j, (x2,y2,z2) in enumerate(boxes):
        if j > i:
            cd = ((x-x2)**2 + (y-y2)**2 + (z-z2)**2)
            dists[cd] = (i, j)

seen = set()

def find_group(i):
    if i in seen: return []
    seen.add(i)
    g = [i]
    for j in connections[i]:
        g += find_group(j)
    return g

for d in sorted(dists.keys()):
    i, j = dists[d]
    connections[i] += [j]
    connections[j] += [i]

    seen = set()
    if len(find_group(0)) == 1000:
        ans = boxes[i][0] * boxes[j][0]
        break

print(f'ans:{ans}')