import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()
# if test: exit()

ans = 0
cs = []

for l in lines:
    x,y = map(int, l.split(','))
    cs.append([x,y])

for i, (x,y) in enumerate(cs):
    for j, (x2,y2) in enumerate(cs):
        v = (abs(x-x2)+1) * (abs(y-y2)+1)
        if test: print(x, y, x2, y2, v)
        ans = max(v, ans)

print(f'ans:{ans}')