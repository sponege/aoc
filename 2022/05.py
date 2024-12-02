#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

## you don't want to print a lot of debug info if you aren't in debug mode!
real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

# some helpful information:
# the variable p stores what part you are currently on, it's either 1 or 2
# make your script work with both parts by using if p == 1: ... else: ...
# the variable d is a boolean; it returns if you are in debug mode or not
# the submit function works 
# the variable t is a boolean; it returns if you are in test mode or not
ans = 'No answer calculated yet'

crates, instructions = inp.split('\n\n')
crates = crates.split('\n')[::-1]
crates.pop(0) #3 dont need those indices

crateParser = lambda line: re.findall('.(.)..', line+' ')
crates = lm(crateParser, crates)

newCrates = []

for _ in range(len(crates[0])):
    newCrate = []
    for crate in crates:
        if crate[_] != ' ': newCrate.append(crate[_])
    newCrates.append(newCrate)

crates = newCrates
print('crates', crates)

instructionReader = lambda line: re.findall('move ([\d]*) from ([\d]*) to ([\d]*)', line)[0]

instructions = lm(instructionReader, instructions.strip().split('\n'))
print(instructions)

for instruction in instructions:
    crateCount = int(instruction[0])
    fromCrate = int(instruction[1])
    toCrate = int(instruction[2])
    print(f'move {crateCount} from {fromCrate} to {toCrate}')
    if p == 1:
        for _ in range(crateCount):
            newCrates[toCrate-1].append(newCrates[fromCrate-1].pop())
    else: ## part 2
        crate = newCrates[fromCrate-1][-crateCount:]
        print('crate', crate)
        newCrates[fromCrate-1] = newCrates[fromCrate-1][:-crateCount]
        newCrates[toCrate-1] += crate
    print(newCrates)


## your code goes here
ans = ''.join(im(-1, newCrates))
if p == 1:
    # ans = 1337
    pass
else: ## part 2
    # ans = 13371337
    pass

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
