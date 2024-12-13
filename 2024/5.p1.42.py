#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
print('read everything')

ans = 0

g = [list(l) for l in lines]
ds=[[0,1],[1,0],[0,-1],[-1,0]]
dsm='^>v<>'
orderings,updates=inp.split('\n\n')

nos=[]
for o in orderings.split('\n'):
    l=o.split('|')
    l=list(map(int,l))
    if len(l):nos+=[l]
orderings=nos


updates=updates.split('\n')
ocp=list(list(o) for o in orderings)
print(ocp)
for l in updates:
    ocp=list(list(o) for o in orderings)
    l=list(map(int, l.split(',')))
    # print(l)
    fail=0
    ci=0
    print(l)
    for t in l:
        i=0
        f=0
        
        while i < len(ocp):
            # print(ocp[i])
            if len(ocp[i]):
                j=0
                # f2=1
                while j < len(ocp[i]):
                    if not all(v in l for v in ocp[i]): break
                    # if test: print(ocp[i][j], l, ocp[i][j] in l)
                    if ocp[i][j] == t:
                        # f2=0
                    
                        if not all(v in l[:ci] for v in ocp[i][:j]):
                            if test: print('ohno', t, ocp[i][:j+1], l[:ci+1])
                            fail=1
                        # else: break
                    
                    j+=1
                # if f2: break
                # if not f2: f=0

            i+=1

        # if f: fail=1; break
        # if len(ocp) > i and len(ocp[i]): ocp[i].pop(0)
        ci+=1
    if not fail: ans += l[len(l)//2]
print(f'ans:{ans}')