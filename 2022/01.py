#!/bin/python3
from util import *

elves = []
curElf = []

while True:
    try:
        line = input()
    except EOFError:
        break
    if line == '':
        elves.append(curElf)
        curElf = []
        continue
    i = int(line)
    curElf.append(i)

elves.append(curElf)

#elves = [sum(calories) for calories in elves]
elves = lm(sum, elves)
#print(elves)
print("Part 1 answer:", max(elves))
#print("Elf", elves.index(max(elves)) + 1)

# Part 2
elves.sort()
print("Part 2 answer:", sum(elves[-3:]))
