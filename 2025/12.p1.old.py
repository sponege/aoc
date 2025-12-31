import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()
if test: exit()
ans = 0

for l in lines[30:]:
    dimensions, *shapes = l.split()
    dimensions = dimensions[:-1]
    shapes = list(map(int, shapes))
    w, h = map(int, dimensions.split('x'))
    
    area = w * h
    # print(w,h,area)

    area -= (shapes[0]) * (3*3)

    area -= (shapes[1]) * (3*4/2)
    # AAA
    # BAA
    # BBA
    # BBB

    area -= (shapes[2]) * (3*3)

    area -= (shapes[3]) * (3*3)

    area -= (shapes[4]) * (3*4/2)
    # AAA.
    # ABBB
    # AAAB
    # .BBB

    area -= (shapes[5]) * (3*3)

    # for s in shapes:
    #     area -= s * (3*2)
    # print(area)
    
    if area >= 0: ans += 1

print(f'ans:{ans}')
