import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

p1 = p2 = 0
d = 50 # dial value
print('read it all')

for l in lines:
    r, v = l[0], int(l[1:])
    od = d # original dial value
    dd = (1 if r == 'R' else -1) * v
    d += dd
    diff = 0

    if d >= 100 or d <= 0:
        if d >= 100:
            diff = d // 100
        else:
            diff = abs(d) // 100
            if od != 0: diff += 1
    p2 += diff
    d %= 100
    if d == 0: p1 += 1
print(p1, p2)