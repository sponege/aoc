import sys, re
from util import *
from collections import deque, defaultdict

from z3 import *

p, d, test, inp, lines = getArgs()

ans = 0

for l in lines:
    goal, *buttons, joltages = l.split()
    goal = goal[1:-1]
    goal = [1 if g == '#' else 0 for g in goal]
    buttons = [ints(b) for b in buttons]
    joltages = ints(joltages)

    s = Optimize()
    final_values = [0 for i in range(len(joltages))]
    button_presses = [Int(i) for i in range(len(buttons))]
    for i, b in enumerate(buttons):
        for j in b:
            final_values[j] += button_presses[i]
        s.add(button_presses[i] >= 0)
    
    for i, joltage in enumerate(joltages):
        s.add(final_values[i] == joltage)
    
    total = 0
    for b in button_presses:
        total += b
    
    s.minimize(total)
    s.check()

    m = s.model()
    v = m.eval(total)
    v = v.as_long()
    ans += v

print(f'ans:{ans}')
