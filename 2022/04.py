#!/bin/python3

import sys
from util import *
inp = sys.stdin.read()
lines = inp.splitlines()
pairs = [[list(map(int,r.split('-'))) for r in pair.split(',')] for pair in lines]
ranges = sum(pairs, []) 

print('Part 1:', sum(list(map(fully_contains,pairs))))
print('Part 2:', sum(list(map(contains,pairs))))

