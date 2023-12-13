#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

ans = 0

def find_reflection(g,dir=0): # grid
    # horizontal
    g=g.split('\n')
    # print(g)
    for i in range(len(g[0])-1):
        for l in g:
            s=1
            k=i
            for j in range(i+1,len(g[0])):
                if l[k] != l[j]:
                    s=0
                    break
                if k==0:break
                k-=1
            if not s: break
        if s:
            yield (i+1)
    
    # vertical
    for i in range(len(g)-1):
        s=1
        k=i
        for j in range(i+1,len(g)):
            # print(g[k], g[j])
            if g[k] != g[j]:
                s=0
                break
            if k==0:break
            k-=1
        if s:
            yield (i+1)*100


def find_smudge(g):
    o=list(map(list,g.split('\n')))

    orig=list(find_reflection(g))[0]

    for x in range(len(o[0])):
        for y in range(len(o)):
            c=[[c for c in l] for l in o]
            c[y][x] = '#' if c[y][x] == '.' else '.'
            vs=list(find_reflection('\n'.join([''.join(l) for l in c])))
            for v in vs:
                if v and v != orig: return v

if p == 1: notes = list(im(0,map(list,map(find_reflection, inp.split('\n\n')))))
if p == 2: notes = list(map(find_smudge, inp.split('\n\n')))

print(notes)
ans = sum(notes)
## submit answer you got to the utils function
final(t, p, ans, expected_ans)
