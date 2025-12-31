import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()
# if not test: exit()

ans = 0

for l in lines:
    goal, *buttons, joltages = l.split()
    goal = goal[1:-1]
    goal = [1 if g == '#' else 0 for g in goal]
    buttons = [ints(b) for b in buttons]
    joltages = ints(joltages)
    
    q = [[[0]*len(goal),0]]
    seen = set()
    while q:
        states, steps = q.pop(0)
        k = ''.join(map(str, states))
        if k in seen: continue
        seen.add(k)
        if test: print(states)
        if states == joltages:
            print('done', steps)
            ans += steps
            break

        for b in buttons:
            new_state = [v for v in states]
            new_steps = steps
            for i in b:
                new_state[i] += 1
            new_steps += 1
            while max(new_state) < min(joltages):
                new_steps += 1
                for i in b:
                    new_state[i] += 1
            # if test: print(b, states, new_state)
            q.append([new_state, new_steps])

    if test: print(goal, buttons, joltages)

print(f'ans:{ans}')
