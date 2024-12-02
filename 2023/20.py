#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

from math import lcm

modules = {}
inv_modules={}
for l in lines:
    module, destinations = l.split(' -> ')
    destinations = destinations.split(', ')
    for d in destinations:
        m = module[1:] if module[0] == '%' or module[0] == '&' else module
        if d in inv_modules: inv_modules[d][m] = 0
        else: inv_modules[d] = {m: 0}
    if module == 'broadcaster':
        modules[module] = ['broadcaster', 0, destinations]
    elif module[0] == '%':
        modules[module[1:]] = ['flipflop', 0, destinations]
    elif module[0] == '&':
        modules[module[1:]] = ['conjunction', -1, destinations]

lp=0 # low pulses
hp=0 # high pulses
rx_modules = inv_modules[list(inv_modules['rx'].keys())[0]].keys()
rx_results = {x: 0 for x in rx_modules}

print(rx_results)

def button(presses):
    global lp, hp
    paths=[[0,'broadcaster','button']]
    while len(paths)>0:
        pulse,name,source=paths.pop(0)
        if pulse: hp += 1
        else: lp += 1
        if name == 'rx' or name == 'output':
            if p == 2 and pulse == 0: return 1
            continue
        t,s,ds=modules[name] # type, state, destinations
        if t == 'broadcaster':
            for d in ds: paths.append([pulse,d,name])
        elif t == 'flipflop':
            if pulse == 0: modules[name][1] = 0 if modules[name][1] else 1
            else: continue
            pulse = modules[name][1]
            for d in ds: paths.append([pulse,d,name])
        elif t == 'conjunction':
            inv_modules[name][source] = pulse
            pulse = 0 if sum(inv_modules[name].values()) == len(inv_modules[name]) else 1
            for d in ds: paths.append([pulse,d,name])
        if name in rx_results and pulse: rx_results[name] = presses=

for _ in range(1000 if p == 1 else 999999): 
    button(_+1)
    if p == 2 and all(rx_results.values()):
        print(rx_results.values(), rx_results)
        ans=lcm(*rx_results.values())
        break
if p == 1: ans=lp*hp

## submit answer you got to the utils function
final(t, p, ans, expected_ans)