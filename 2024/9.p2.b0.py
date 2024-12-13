#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
inp=inp.strip()
print('read everything')

filesystem = []
fsm = {}
for i in range(len(inp)):
    filesystem += [i//2 if i%2==0 else -1] * int(inp[i])
    if i % 2 == 0: fsm[i//2] = int(inp[i])
print(fsm)

for real_target in sorted(fsm.keys(), reverse=1):
    print(real_target)
    for i in [j for j in range(len(filesystem)) if filesystem[j] == -1 and (j == 1 or filesystem[j-1] != -1)]:
        if filesystem[i] == -1:
            c=1
            while i+c-1 < len(filesystem) and filesystem[i+c-1] == -1:
                c+=1
            # if i+c-1 >= len(filesystem): c-=1
            c-=1
            j=len(filesystem)
            # list_thing = [(k,v) for k,v in fsm.items() if k == real_target]
            # if len(list_thing) == 0: continue
            # target,nc = list_thing[0]
            target,nc = real_target,fsm[real_target]
            # print(c, target)
            c = min(c, nc)
            # print(c, target)
            while 1:
                j-=1
                if j > 0 and filesystem[j] != target: continue
                if fsm[filesystem[j]] <= c: break
                if j <= 0: break
                # if test: print(j)
            if j > i:
                for k in range(c):
                    # if test: print(j, k, c)
                    filesystem[i+k] = filesystem[j-k]
                    filesystem[j-k] = -1
                del fsm[target]
                break
            
        # if test: print(filesystem)

print(filesystem[:50],j,filesystem[j])
print(len(filesystem))
ans=sum(i*filesystem[i] for i in range(len(filesystem)) if filesystem[i] != -1)
print(f'ans:{ans}')