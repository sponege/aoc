import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0

for l in lines:
    cm = 0
    for i, c in enumerate(l):
        for j, c2 in enumerate(l):
            if j > i: cm = max(cm, int(c+c2))
    print(cm)
    ans += cm
    

print(f'ans:{ans}')