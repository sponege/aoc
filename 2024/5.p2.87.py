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
# print(ocp)

from functools import cmp_to_key

for l in updates:
    ocp=list(list(o) for o in orderings) # orderings copy
    l=list(map(int, l.split(',')))
    # print(l)
    fail=0
    ci=0
    # print(l)
    if test: print(l)
    for t in l:
        i=0
        f=0
        oci=ci

        
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
                        for v in ocp[i][:j]:
                            if v in l[ci+1:]:
                                # fail=1
                                # vi=ocp[i].index(v)
                                # l=[0]
                                fail=1
                                # if all(v2 in l for v2 in ocp[i][:j]):
                                # nl=l[:ci]
                                # nl+=[v]
                                # nl+=[t]
                                # nl+=list(filter(lambda b: b!=v and b!=t, l[ci+1:]))
                                # l=nl
                                # if test: print('a',nl)
                                # ci+=1
                                # l=list(filter(lambda b: b!=v, l))
                                # l.insert(ci-2, v)
                                # if test: print(v, 'wow')
                                pass
                        # if not all(v in l[:ci] for v in ocp[i][:j]):
                        #     if test: print('ohno', t, ocp[i][:j+1], l[:ci+1])
                        #     fail=1
                        #     l.insert()

                        # else: break
                    
                    j+=1
                # if f2: break
                # if not f2: f=0
            i+=1

        # if f: fail=1; break
        # if len(ocp) > i and len(ocp[i]): ocp[i].pop(0)
        ci=oci
        ci+=1
    while 1:
        vol=list(l) # very old list
        for cl in ocp:
            if all(v2 in l for v2 in cl): 
                # cpl=list(l)
                if test: print(cl)
                l.sort(key=cmp_to_key(lambda a,b: (-1 if cl==[a,b] else 1) if a in cl and b in cl else 0))
                # pass
        if vol == l: break
    # l.sort(lambda v: sum(cl.index(v) if v in cl else 0 for cl in ocp))
    middle=l[len(l)//2]
    if fail: ans += middle; print(middle)
    if test: print(l)
print(f'ans:{ans}')