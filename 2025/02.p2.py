import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0

for l in inp.split(','):
    s, e = map(int, l.split('-'))
    for i in range(s, e+1):
        s = str(i)
        yes = 0
        for co in range(1, len(s)+1):
            ysf = 1 if range(0, (len(s) // co) - 1) else 0
            if len(s) % co != 0: continue
            for j in range(0, (len(s) // co) - 1):
                if s[j*co:(j*co)+co] != s[(j*co)+co:(j*co)+(co*2)]:
                    ysf = 0
                    break
            if ysf: yes = 1
            if yes: break
        if yes:
            ans += i

    

print(f'ans:{ans}')