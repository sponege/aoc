#!/bin/python3

# this video is sponsored by taco bell

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=0

inp=inp.strip()
print('read everything')

from collections import deque

def mix(v, sn):
    return v ^ sn

def prune(sn):
    return sn % 16777216

prices = []
changes = []

for t in lines:
    sn = int(t)
    first_2000 = []
    
    first_2000.append(sn%10)
    for i in range(2000):
        sn = prune(mix(sn*64, sn))
        sn = mix(sn//32, sn)
        sn = prune(sn)
        sn = mix(sn*2048, sn)
        sn = prune(sn)
        
        first_2000.append(sn%10)
    prices += [first_2000]
    changes += [[first_2000[i]-first_2000[i-1] for i in range(1, 2001)]]

    if test: print(sn)
    # ans += sn
# print(changes[0])
maxbananas = 0

# if not test: exit()

for x in range(-10, 10):
    print(f'{x=}')
    for y in range(-10, 10):
        print(f'{y=}')
        for z in range(-10, 10):
            print(f'{z=}')

            for a in range(-10, 10):
                
                bananas = 0
                for j,cl in enumerate(changes):
                    for i in range(1997):
                        if cl[i] == x and cl[i+1] == y and cl[i+2] == z and cl[i+3] == a:
                            bananas += prices[j][i+4]
                            break
                # if bananas > maxbananas:
                #     print(x, y, z, a, bananas)
                maxbananas = max(bananas, maxbananas)
ans = maxbananas

print(f'ans:{ans}')
