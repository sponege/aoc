#!/bin/python3
import sys
inp = sys.stdin.read()
lines = inp.splitlines()

cycles = 0
X = 1

strengths = []

def cycle():
    global cycles, X
    cycles += 1
    imp_cycles = [20, 60, 100, 140, 180, 220]
    if cycles in imp_cycles:
        #print('{}*{} = {}'.format(cycles, X, X*cycles))
        strengths.append(X*cycles)
    x = cycles % 40
    #c = '█' if x>=X and x<X+3 else ' '
    c = '#' if x>=X and x<X+3 else ' '
    print(c, end = '')
    if x == 0:
        print()

## part 1
for line in lines:
    line = line.strip()
    if line == '': continue
    if line == 'noop':
        cycle()
        continue
    ins, val = line.split()
    val = int(val)
    if ins == 'addx':
        for _ in range(2):
            cycle()
        X += val
#print("p1", sum(strengths))
