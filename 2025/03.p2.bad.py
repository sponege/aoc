import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0
# if not test: exit()

for index, l in enumerate(lines):
    
    ps = [[0,0,12]]
    cm = 0

    maxes = defaultdict(int)
    it = 0
    while len(ps):
        # if it % 100000 == 0: print(len(ps), ps[0])
        i, s, b = ps.pop(0)
        if s < maxes[b]: continue
        cm = max(cm, s)
        maxes[b] = max(maxes[b], s)
        if b > 0:
            if i >= len(l): continue
            v = 10*(s+int(l[i]))
            maxes[b-1] = max(v, maxes[b-1])
            if v >= maxes[b-1]: ps.append([i+1,v,b-1])
            if s >= maxes[b]: ps.append([i+1,s,b])
        it += 1
        # print(cm)
    cm //= 10
    print(index, cm)
    ans += cm
    

print(f'ans:{ans}')