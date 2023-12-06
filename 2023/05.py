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
    # seeds=list(filter(lambda a: a is not None, seeds))
if p == 2:
    for i, s in enumerate(seeds):
        if i%2==1:
            seeds[i]+=seeds[i-1]-1
            seeds[i-1]=[seeds[i-1],seeds[i]]
            seeds[i]=None
    seeds=list(filter(lambda a: a is not None, seeds))
print(seeds)

def process(s,m):
    if p == 1:
        for mapping in m:
            if s>=mapping[1] and s<mapping[1]+mapping[2]:
                return s-mapping[1]+mapping[0]
        return s
    else:
        new_seeds=[]
        for seed_range in s:
            for mapping in m:
                if seed_range[0] >= mapping[1] and seed_range[0] < mapping[1]+mapping[2]:
                    seed_range[0]=seed_range[0]-mapping[1]+mapping[0]
                    if seed_range[1] > mapping[1]+mapping[2]:
                        new_seeds.append([seed_range[0],mapping[0]+mapping[2]-1])
                        seed_range[0]=mapping[1]+mapping[2]
                if seed_range[1] >= mapping[1] and seed_range[1] < mapping[1]+mapping[2]:
                    seed_range[1]=seed_range[1]-mapping[1]+mapping[0]
                    if seed_range[0] < mapping[1]:
                        new_seeds.append([mapping[0],seed_range[1]])
                        seed_range[1]=mapping[1]-1
            new_seeds.append(seed_range)
            s=new_seeds
        return s
                

maps=[[[int(n) for n in r.findall(ns)] for ns in ls.split('\n')[1:]] for ls in inp.split('\n\n')[1:]]
for m in maps:
    if p == 1: seeds = [process(s,m) for s in seeds]
    else: seeds = process(seeds,m)
    print(sorted(seeds))
if p == 2: seeds = [s[0] for s in seeds]
ans = min(seeds)

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
