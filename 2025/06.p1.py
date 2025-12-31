import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0
# g = [list(l) for l in lines]

# if not test: exit()

ops = list(c for c in lines[-1] if c in '+*')

ns = []

for l in lines[:-1]:
    n = ints(l)
    ns += [n]

ns = list(zip(*ns))
print(ns)

def mul(l):
    a = 1
    for i in l:
        a *= i
    return a

for i in range(len(ops)):
    if ops[i] == '*':
        ans += mul(ns[i])
    else:
        ans += sum(ns[i])

print(f'ans:{ans}')