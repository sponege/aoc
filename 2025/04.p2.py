import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0
# if not test: exit()
g = [list(l) for l in lines]

def get(x,y):
    if x < 0 or x >= len(g[0]) or y < 0 or y >= len(g): return '.'
    else: return g[y][x]

while 1:
    r = 0
    for x in range(len(g[0])):
        for y in range(len(g)):
            if get(x,y) != '@': continue
            cc = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    cx, cy = x+dx, y+dy
                    if get(cx,cy) == '@': cc += 1
            if cc < 5:
                print(x,y,cc)
                ans += 1
                g[y][x] = '.'
                r = 1
    if not r: break

print(f'ans:{ans}')