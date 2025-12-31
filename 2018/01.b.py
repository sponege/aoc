import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()


ans = 0
c = 0
s = set()

while ans == 0:
    for v in ints(inp):
        c += v
        if c in s:
            ans = c
            break
        s.add(c)

print(f'ans:{ans}')