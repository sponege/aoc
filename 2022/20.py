#!/bin/python3

import sys
from util import *
inp = sys.stdin.read()
lines = inp.splitlines()

global p, d
applyKey = lambda num: num * (811589153 if p == 2 else 1)
coords = list(enumerate(
lm(applyKey,
    lm(int, lines)
   )
))

print(coords)
print()
rounds = (10 if p == 2 else 1)
cc = coords.copy()
for i in range(rounds):
    for key, val in cc:

        #pos = (pos + i) % len(coords)
        pos = coords.index((key, val))
        val2 = coords.pop(pos)

        assert val == val2[1]
        insertLoc = (pos + val) % len(coords)

        coords.insert(insertLoc, (key,val))
        print([c[1] for c in coords])
    print()


def search(list, platform):
    for i in range(len(list)):
        if list[i][1] == platform:
            return i
    return False

def getPosition(pos, coords):
    pos += search(coords, 0)
    return coords[pos%len(coords)][1]
a=[getPosition(1000, coords), getPosition(2000, coords), getPosition(3000, coords)]
p([c[1] for c in coords])
p(a)
ans=sum(a)
p(ans)

