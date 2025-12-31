import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0

for l in lines:
    n = list(map(int, l.split()))
    ans += max(n) - min(n)

print(f'ans:{ans}')