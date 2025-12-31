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
        minx = min(x,x2)
        maxx = max(x,x2)
        miny = min(y,y2)
        maxy = max(y,y2)
        v = (abs(x-x2)+1) * (abs(y-y2)+1)
        # if test: print(x, y, x2, y2, v)
        valid = 1
        for k in range(0, len(cs)):
            # if k + 1 >= len(cs): continue
            first = cs[k]
            second = cs[(k+1)%len(cs)]
            if (((first[0] <= minx and second[0] > minx) or (first[0] >= maxx and second[0] < maxx)) and \
                (first[1] > miny and first[1] < maxy)) or \
                (((first[1] <= miny and second[1] > miny) or (first[1] >= maxy and second[1] < maxy)) and \
                 (first[0] > minx and first[0] < maxx)):
                valid = 0
                break
        if valid:
            # if v > ans:
            #     print(x,y,x2,y2)
            ans = max(v, ans)

print(f'ans:{ans}')