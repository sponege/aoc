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

## your code goes here

ans = 0
if p == 1:
    # ans = 1337
    for line in lines:
        rucksack_one = line[:len(line) // 2]
        rucksack_two = line[len(line) // 2:]
        #print(rucksack_one, rucksack_two)
        for item in rucksack_one:
            if item in rucksack_two:
                print(item)
                ans += ord(item) - ord('a') if item.islower() else ord(item) - ord('A') + 26
                break
    ans += len(lines)
    pass
else: ## part 2
    groups = []
    while len(lines) > 0:
        group = []
        for _ in range(3):
            group.append(lines.pop(0))
        groups.append(group)

    for group in groups:
        rucksack_one = group[0]
        rucksack_two = group[1]
        rucksack_three = group[2]
        #print(rucksack_one, rucksack_two)
        for item in rucksack_one:
            if item in rucksack_two and item in rucksack_three:
                print(item)
                ans += ord(item) - ord('a') if item.islower() else ord(item) - ord('A') + 26
                break
    ans += len(groups)
    # ans = 13371337
    pass

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
