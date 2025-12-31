import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

t = int(inp)

ans = 0

v = 3
c = 2
di = 0
ds=[[-1,0],[0,-1],[1,0],[0,1]]

x = 1
y = 1

while 1:
    for _ in range(2):
        dx, dy = ds[di]
        x += dx * min(c, t-v)
        y += dy * min(c, t-v)
        v += min(c, t-v)
        di += 1
        di %= 4
    c += 1

    if v == t: break

print(x,y)

ans = abs(x) + abs(y)

print(f'ans:{ans}')