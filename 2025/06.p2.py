import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0
# g = [list(l) for l in lines]

# if not test: exit()
print(list(zip(*lines[:-1])))

new_lines = []

for c in list(zip(*lines[:-1])):
    new_lines += [''.join(c)]

ops = list(c for c in lines[-1] if c in '+*')

numbers = []

for l in new_lines:
    n = ints(l)
    numbers += [n]

# ns = list(zip(*ns))
print(numbers)
exit()

def mul(l):
    a = 1
    for i in l:
        a *= i
    return a
numbers += [[]]
cl = []
i = 0
for j in range(len(numbers)):
    v = numbers[j]
    if len(v):
        cl += v
    else:
        print(cl, ops[i])
        if ops[i] == '*':
            ans += mul(cl)
        else:
            ans += sum(cl)
        i += 1
        cl = []

print(f'ans:{ans}')