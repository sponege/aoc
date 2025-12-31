import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0


for l in inp.split(','):
    s, e = map(int, l.split('-'))
    for i in range(s, e+1):
        s = str(i)
        if s[:len(s)//2] == s[len(s)//2:]:
            ans += i
    

print(f'ans:{ans}')