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

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


for l in lines:
    args = l.split(': ')
    ins, vals = args[0], args[1].split(' ')
    ins = int(ins)
    vals = list(map(int, vals))
    # for ops in ['+*' for i in range(len(vals))]:
    #     eva=''
    #     for i in range()
    for i in range((3**(len(vals)-1))):
        ops=''.join(map(str,numberToBase(i,3))).zfill(len(vals)-1).replace('0','*').replace('1','+').replace('2','|')
        result=vals[0]
        for j in range(len(ops)):
            # eval_this += str(vals[j+1])+')'+ops[j]
            operator = ops[j]
            if operator == '+': result += vals[j+1]
            if operator == '*': result *= vals[j+1]
            if operator == '|': result = int(str(result)+str(vals[j+1]))
        # eval_this=eval_this[:-1]
        # eval_this += str(vals[len(vals)-1])+')'
        # print(eval_this)
        # print(ops, vals, result)

        if result == ins:
            ans += ins
            if test: print(result, ins)
            break


print(f'ans:{ans}')