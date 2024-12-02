#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

## you don't want to print a lot of debug info if you aren't in debug mode!
real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

import re
r=re.compile(r'(\d+)')
ans = 0

seeds = [int(n) for n in r.findall(lines[0].split(': ')[1])]
# if p == 1:
#     new_seeds=[]
#     for i, s in enumerate(seeds):
#         if i%2==1:
#             seeds[i]+=seeds[i-1]-1
#             for i in range(seeds[i-1],seeds[i]+1): new_seeds.append(i)
#     seeds=new_seeds
#     print(seeds)
#     seeds=list(filter(lambda a: a is not None, seeds))
if p == 2:
    for i, s in enumerate(seeds):
        if i%2==1:
            seeds[i]+=seeds[i-1]-1
            seeds[i-1]=[seeds[i-1],seeds[i]]
            seeds[i]=None
    seeds=list(filter(lambda a: a is not None, seeds))
print(seeds)

def process(seeds,m):
    if p == 1:
        for a,b,c in m:
            if s>=b and s<b+c:
                return s-b+a
        return seeds
    else:
        new_seeds=[]
        while len(seeds) > 0:
            s,e = seeds.pop()
            for a,b,c in m:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    new_seeds.append([os - b + a, oe - b + a])
                    if os > s:
                        seeds.append([s, os])
                    if e > oe:
                        seeds.append([oe, e])
                    break
            else:
                new_seeds.append([s, e])
        return new_seeds
                

maps=[[[int(n) for n in r.findall(ns)] for ns in ls.split('\n')[1:]] for ls in inp.split('\n\n')[1:]]
for m in maps:
    if p == 1: seeds = [process(s,m) for s in seeds]
    else: seeds = process(seeds,m)
    print(sorted(seeds))
if p == 2: seeds = [s[0] for s in seeds]
ans = min(seeds)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)