import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 1

boxes = []

dists = {}

groups = []

connections = defaultdict(list)

for loop_count in lines:
    x,y,z = map(int, loop_count.split(','))
    boxes.append((x,y,z))

for i, (x,y,z) in enumerate(boxes):
    for j, (x2,y2,z2) in enumerate(boxes):
        if j > i:
            cd = ((x-x2)**2 + (y-y2)**2 + (z-z2)**2)
            dists[cd] = (i, j)

loop_count = 10 if test else 1000
current_loop_count = 0
for d in sorted(dists.keys()):
    i, j = dists[d]
    connections[i] += [j]
    connections[j] += [i]
    current_loop_count += 1
    if current_loop_count >= loop_count: break

if test: print(connections)

lgroups = []

seen = set()

def find_group(i):
    if i in seen: return []
    seen.add(i)
    g = [i]
    for j in connections[i]:
        g += find_group(j)
    return g

# if test: print(find_group(0))
for i in range(20 if test else 1000):
    g = find_group(i)
    if len(g): lgroups.append(len(g))

lgroups.sort(reverse=1)

for loop_count in lgroups[:3]:
    print(loop_count)
    ans *= loop_count
# if test: print(sorted(dists.keys()))
print(f'ans:{ans}')