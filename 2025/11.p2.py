import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0

c = defaultdict(list)

for l in lines:
    source, *dests = l.split()
    source = source[:-1]
    c[source] += dests

dp = {}
def get(p, path = []):
    key = (p+''.join(path))
    if key in dp:
        return dp[key]
    if p == 'out':
        if 'fft' in path and 'dac' in path: return 1
        return 0
    v = 0
    for d in c[p]:
        if d in ['fft','dac']: v += get(d, path + [d])
        else: v += get(d, path)
    dp[key] = v
    return v
ans = get('svr')

print(f'ans:{ans}')
