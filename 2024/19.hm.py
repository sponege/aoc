#!/bin/python3

# this video is sponsored by taco bell

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=0

inp=inp.strip()
print('read everything')

g = [list(l) for l in lines]

ans=0
d2=[[0,1],[-1,0],[0,-1],[1,0]]
def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

def get(x,y,g):
    if check(x,y): return g[y][x]
    else: return 0

towels = lines[0].split(', ')

lines=lines[2:]
from collections import deque

if not test: exit()

for towel in lines:
    # print(towel)
    ps = deque([[towel, [], []]])
    dp={}
    while ps:
        ct, path, towelsused = ps.popleft()
        # if test: print(towelsused)
        die=0
        if len(ct) == 0:
            print(towelsused)
            print(dp)
            for i in range(1, len(path)):
                key = ','.join(str(z) for z in path[:i])
                print(key)
                ans += dp[key]
            # for z in path: dp[key] += 1
            # break
            pass
        for i in range(1, len(path)+1):
            key = ','.join(str(z) for z in path[:i])
            # print(key)
        # print(len(ps))
        # print(key)
            if key in dp:
                if dp[key] != 1: die=1

                dp[key] += 1
            else: dp[key] = 0
        print(towelsused, die)
        if die and len(towelsused) > 0:
            # print('wow!', towelsused)
            continue
        # for i in range(len(towelsused)):
        #     key = ','.join(z for z in towelsused[:i])
        #     # print(key)
        #     dp[key] = 0
        # print(ct, 'ct')

        for t in towels:
            if ct.startswith(t):
                ps.append([ct[len(t):], path + [len(ct)], towelsused + [t]])
    
    # ans += sum(dp[z] for z in dp)

    if test and 1:
        print(ans)
        print(dp)
print(f'ans:{ans}')
