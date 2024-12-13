#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
print('read everything')
g = [list(l) for l in lines]
ans = 0
# w=len(g[0])
# h=len(g)

g = [list(l) for l in lines]
ds=[[0,-1],[1,0],[0,1],[-1,0]]
dsm='^>v<>'
dc=0

ans=0

for l in lines:
    args = l.split(': ')
    ins, vals = args[0], args[1].split(' ')
    ins = int(ins)
    vals = list(map(int, vals))
    # for ops in ['+*' for i in range(len(vals))]:
    #     eva=''
    #     for i in range()
    for i in range((2**(len(vals)))):
        ops=bin(i)[2:].zfill(len(vals)).replace('0','*').replace('1','+')
        eval_this = '('*(len(ops))
        for j in range(len(ops)):
            eval_this += str(vals[j])+')'+ops[j]
        eval_this=eval_this[:-1]
        # eval_this += str(vals[len(vals)-1])+')'
        # print(eval_this)
        if eval(eval_this) == ins:
            ans += ins
            if test: print(eval_this, ins)
            break


print(f'ans:{ans}')