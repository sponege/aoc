import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0
# g = [list(l) for l in lines]
# aint no way today is gonna be another grid problem lol

# if not test: exit()

fr, ids = inp.split('\n\n')

fresh = []
for l in fr.splitlines():
    a, b = map(int, l.split('-'))
    fresh.append((a,b))

for l in ids.splitlines():
    i = int(l)
    y = 0
    for s, e in fresh:
        if s <= i <= e:
            y = 1
            break
    if y: ans += 1

print(f'ans:{ans}')