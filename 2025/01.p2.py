import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0
d = 50

import math
# for s in inp.split('\n\n'):
for l in lines:
    # ans += 
    r, v = l[0], int(l[1:])
    od = d
    dd = (1 if r == 'R' else -1) * v
    d += dd
    diff = 0
    # print(l, od, d)
    # if (od < 0 and d > 0) or (od > 0 and d < 0) or (d > 100 and od < 100) or (d < -100 and od > -100) or d == 0 or d == 100 or d == -100:
    #     cd = d % 100

    if d >= 100 or d <= 0:
        if d >= 100:
            diff = d // 100
        else:
            diff = abs(d) // 100
            if od != 0: diff += 1

    # if d != d % 100:
    #     diff += abs(d // 100)
    # ans += diff
    # print(l, diff, d)
    ans += diff
    d %= 100
    # if d == 0: ans += 1
    # if test: print(r, v)


print(f'{ans}')