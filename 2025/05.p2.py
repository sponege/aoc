import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

ans = 0
# g = [list(l) for l in lines]
# aint no way today is gonna be another grid problem lol

# if not test: exit()

fr, ids = inp.split('\n\n')

fresh = []
for l in fr.splitlines():
    a, b = map(int, l.split('-'))
    fresh.append([a,b])

inv = set()

while 1:
    nc = 1
    for i, (s, e) in enumerate(fresh):
        for j, (s2, e2) in enumerate(fresh):
            if i == j: continue
            if i in inv or j in inv: continue
            if s2 <= s <= e <= e2:
                nc = 0
                inv.add(i)
            if s <= s2 <= e <= e2:
                nc = 0
                fresh[i][1] = s2 - 1
            if s2 <= s <= e2 <= e:
                nc = 0
                fresh[i][0] = e2 + 1
            if nc == 0: break
        if nc == 0: break
    if nc: break
print(inv, fresh)

for i, (s, e) in enumerate(fresh):
    if i not in inv:
        print(s, e, e - s + 1)
        ans += e - s + 1
# for l in ids.splitlines():
#     i = int(l)
#     y = 0
#     for s, e in fresh:
#         if s <= i <= e:
#             y = 1
#             break
#     if y: ans += 1

print(f'ans:{ans}')