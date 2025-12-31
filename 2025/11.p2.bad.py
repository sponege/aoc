import sys, re
from util import *
from collections import deque, defaultdict

from z3 import *

p, d, test, inp, lines = getArgs()

ans = 0

c = defaultdict(list)
if not test: exit()

for l in lines:
    source, *dests = l.split()
    source = source[:-1]
    # if test: print(source, dests)
    c[source] += dests

# if test: print(c)


q = [['svr',set()]]
while q:
    p, seen = q.pop()
    k = p
    if k in seen: continue


    if p == 'out' and 'dac' in seen and 'fft' in seen: ans += 1
    
    seen.add(k)
    for d in c[p]:
        q.append([d,seen|set()])

print(f'ans:{ans}')
