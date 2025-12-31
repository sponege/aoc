import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()

t = int(inp)

ans = 0

v = 3
c = 2
di = 0
ds=[[-1,0],[0,-1],[1,0],[0,1]]

x = 1
y = 1

g = defaultdict(int)

g[(0,0)] = 1
g[(1,0)] = 1
g[(1,1)] = 2

loop = 1

while loop:
    for _ in range(2):
        dx, dy = ds[di]
        for _2 in range(c):
            x += dx
            y += dy
            cv = 0
            for lx in range(-1, 2):
                for ly in range(-1, 2):
                    cv += g[(x+lx,y+ly)]
            g[(x,y)] = cv
            if cv > t:
                ans = cv
                loop = 0
                break
        if not loop: break

        di += 1
        di %= 4
    c += 1

    # if v == t: break
print(x,y)

print(g[(1,0)])

# ans = abs(x) + abs(y)
print(t,ans)
print(f'ans:{ans}')