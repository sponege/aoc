import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0

for l in lines:
    n = list(map(int, l.split()))

    d = 1
    for a in n:
        for b in n:
            if a%b == 0 and a != b:
                ans += a//b
                d = 0
                break
        if d == 0: break
    # ans += max(n) - min(n)

print(f'ans:{ans}')