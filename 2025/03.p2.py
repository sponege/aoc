import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0
# if not test: exit()

for index, l in enumerate(lines):
    l = list(map(int, list(l)))
    ci = 0
    v = 0
    for i in range(12):
        # print(l[ci:len(l)-(11-i)])
        m = max(l[ci:len(l)-(11-i)])
        # print(m)
        ci += l[ci:].index(m) + 1
        v += m
        v *= 10
    v //= 10
    # print(v)
    ans += v
    

print(f'ans:{ans}')