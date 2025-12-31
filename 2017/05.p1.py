import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0

i = 0
l = list(map(int, inp.split()))

while 0 <= i < len(l):
    ans += 1
    oi = i
    i += l[i]
    l[oi] += 1


print(f'ans:{ans}')