import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0

c = defaultdict(list)

for l in lines:
    source, *dests = l.split()
    source = source[:-1]
    c[source] += dests

q = [['you',set()]]
while q:
    p, seen = q.pop()
    k = p
    if k in seen: continue
    seen.add(k)

    if p == 'out': ans += 1
    
    for d in c[p]:
        q.append([d,seen|set()])

print(f'ans:{ans}')