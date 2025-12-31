import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0

for l in lines:
    if len(set(''.join(sorted(w)) for w in l.split())) != len(l.split()): continue
    ans += 1

print(f'ans:{ans}')