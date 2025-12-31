import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()
ans = 0

for l in lines:
    if 'x' not in l: continue

    dimensions, *shapes = l.split()
    dimensions = dimensions[:-1]
    shapes = list(map(int, shapes))
    w, h = map(int, dimensions.split('x'))
    
    area = w * h
    for s in shapes:
        area -= s * (3*3)
    
    if area >= 0: ans += 1

print(f'ans:{ans}')
