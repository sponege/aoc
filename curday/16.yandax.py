#!/bin/python3
import sys, re
from collections import deque, defaultdict
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=float('inf')

inp=inp.strip()
print('read everything')
# if not test: exit()

start = findLetter('S', lines)
end = findLetter('E', lines)

right_map = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
left_map = {(0, 1): (-1, 0), (1, 0): (0, 1), (0, -1): (1, 0), (-1, 0): (0, -1)}

import heapq
def dijkstra(grid, start, end):
    dir = (0, 1)
    q = [(0, start, dir, set([start]))]
    heapq.heapify(q)
    opt_score = float('inf')
    ans_set = set()
    dist_map = defaultdict(lambda: float('inf'))
    while len(q) > 0:
        dist, pos, dir, path = heapq.heappop(q)
        while len(q) > 0:
            dist1, pos1, dir1, path1 = heapq.heappop(q)
            if (dist1, pos1, dir1) != (dist, pos, dir):
                heapq.heappush(q, (dist1, pos1, dir1, path1))
                break
            path |= path1

        dist_map[(pos, dir)] = min(dist_map[(pos, dir)], dist)
        if dist > opt_score:
            return opt_score, ans_set
        if pos == end:
            opt_score = min(opt_score, dist)
            ans_set |= path
        if dist > dist_map[(pos, dir)]:
            continue
        
        # forward, right, left
        nxt = (pos[0]+dir[0], pos[1]+dir[1])
        if grid[nxt[0]][nxt[1]] != '#':
            heapq.heappush(q, (dist+1, nxt, dir, path | {nxt}))
        heapq.heappush(q, (dist+1000, pos, right_map[dir], path))
        heapq.heappush(q, (dist+1000, pos, left_map[dir], path))

a,b = dijkstra([list(l) for l in lines], start, end)
b = len(b)
ans = (a,b)
print(f'ans:{ans}')
