import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()
ans = 0
days = 2001

gifts_total = 0
gifts_today = 1
for _ in range(days):
    gifts_total += gifts_today
    ans += gifts_total
    gifts_today += 1

print(f'ans:{ans}')
