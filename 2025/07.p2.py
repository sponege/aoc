import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0


g = [list(l) for l in lines]
def find(c):
    for y in range(len(g)):
        if c in g[y]: return (g[y].index(c), y)
def get(x,y):
    if x < 0 or x >= len(g[0]) or y < 0 or y >= len(g): return '!'
    else: return g[y][x]
# if not test: exit()

w = len(g[0])
h = len(g)
sx, sy = find('S')
dp = [[0] * w for _ in range(h)]
dp[0][sx] = 1
p1 = 0
for y in range(h - 1):
    for x in range(w):
        if not (v := dp[y][x]):
            continue
        if g[y+1][x] == '^':
            p1 += 1

            dp[y+1][x+1] += v
            dp[y+1][x-1] += v
        else:
            dp[y+1][x] += v
ans = sum(dp[-1])
print(dp)

# print(ps)
print(f'ans:{ans}')