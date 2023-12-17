#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

# thank you HyperNeutrino!
from heapq import heappush, heappop
grid = [list(map(int, line.strip())) for line in lines]

seen = set()
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    hl, r, c, dr, dc, n = heappop(pq)
    # heat loss, row, column, difference in row, difference in column, steps taken

    if r == len(grid) - 1 and c == len(grid[0]) - 1 and (n >= 4 or p == 1):
        ans = hl
        break

    if (r, c, dr, dc, n) in seen:
        continue

    seen.add((r, c, dr, dc, n))

    if n < (3 if p == 1 else 10) and (dr, dc) != (0, 0):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))
    
    if p == 1 or n >= 4 or (dr, dc) == (0, 0):
        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))

## submit answer you got to the utils function
final(t, p, ans, expected_ans)