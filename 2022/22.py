#!/bin/python3

import sys, re, time
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

## you don't want to print a lot of debug info if you aren't in debug mode!
real_print = print
if not d:
    print = lambda *args, **kwargs: None
    time.sleep = lambda *args, **kwargs: None

addPosToMap = lambda pos, map: '\n'.join(map[max(0,pos[1]-2):pos[1]] + [map[pos[1]][:pos[0]] + 'X' + map[pos[1]][pos[0]+1:]] + map[pos[1]+1:pos[1]+3])
#addPosToMap = lambda pos, map: '\n'.join(map[:pos[1]] + [map[pos[1]][:pos[0]] + 'X' + map[pos[1]][pos[0]+1:]] + map[pos[1]+1:])
# some helpful information:
# the variable p stores what part you are currently on, it's either 1 or 2
# make your script work with both parts by using if p == 1: ... else: ...
# the variable d is a boolean; it returns if you are in debug mode or not
# the submit function works 
# the variable t is a boolean; it returns if you are in test mode or not
ans = 'No answer calculated yet'
convDir = lambda d: (int(d[0]), d[1])

lastline = lines[-1]
print(lastline)
instructions = lm(convDir, re.findall(r'([\d]*)([A-Z])', lastline))
instructions.append((29, 'X'))
map = lines[:-2]
# real_print(instructions)

pos = [map[0].index('.'), 0]
d = [1, 0]

_=0
def visual(_p,extra=''):
    global _
    # clear screen with escape code
    try:
        if _p[0] < 0 or _p[1] < 0 or _p[0] >= len(map[_p[1]]) or _p[1] >= len(map):
            return
    except:
        return
    print('\033[2J')
    print(extra)
    _+=1
    print(_p, 'moving', d, _)
    print(addPosToMap(_p,map))
    time.sleep(.2)


def mvdxdy(p, dx, dy):
    assert abs(dx) + abs(dy) == 1
    p = [p[0] + dx, p[1] + dy]
    visual(p)
    try:
        if map[p[1]][p[0]] != ' ' and p[0] >= 0 and p[1] >= 0 and p[0] < len(map[p[1]]) and p[1] < len(map):
            return p
    except:
        pass
        """
        if p[1] < 0:
            p[1] = len(map) - 1
        elif p[1] >= len(map):
            p[1] = 0
        if p[0] < 0:
            p[0] = len(map[p[1]]) - 1
        elif p[0] >= len(map[p[1]]):
            p[0] = 0
        """
    p = [p[0] - dx, p[1] - dy]
    while map[p[1]][p[0]] != ' ':
        p = [p[0] - dx, p[1] - dy]
        if p[1] < 0:
            break
        elif p[1] >= len(map):
            break
        if p[0] < 0:
            break
        elif p[0] >= len(map[p[1]]):
            break
        visual(p,'searching')
    p = [p[0] + dx, p[1] + dy]
    visual(p,'found')
    return p

def move(steps, dxy):
    global pos
    # dxy is a tuple of (dx, dy)
    # steps is the number of steps to move
    # returns the new position
    for _ in range(steps):
        if p == 1:
            pos = mvdxdy(pos, dxy[0], dxy[1])
            if map[pos[1]][pos[0]] == '#':
                # move back
                pos = mvdxdy(pos, -dxy[0], -dxy[1])
        else: ## part 2
            pass
        continue 
        """
        if dir == 'L':
            pos[0] -= 1
            if map[pos[1]][pos[0]] != '.':
                pos[0] += 1
                if pos[0] >= len(map[0]):
                    pos[0] = 0
            if map[pos[1]][pos[0]] == ' ':
                pos[0] += 1
                if pos[0] >= len(map[0]):
                    pos[0] = 0
                    while map[pos[1]][pos[0]] != ' ':
                        pos[0] += 1
                pos[0] -= 1
        elif dir == 'R':
            pos[0] += 1
            if pos[0] >= len(map[0]):
                pos[0] = 0
            if map[pos[1]][pos[0]] != '.':
                pos[0] -= 1
                if pos[0] < 0:
                    pos[0] = len(map[0]) - 1
            if map[pos[1]][pos[0]] == ' ':
                pos[0] -= 1
                if pos[0] < 0:
                    pos[0] = len(map[0]) - 1
                    while map[pos[1]][pos[0]] != ' ':
                        pos[0] -= 1
                pos[0] += 1
        elif dir == 'U':
            pos[1] -= 1
            if pos[1] < 0:
                pos[1] = len(map) - 1
            if map[pos[1]][pos[0]] != '.':
                pos[1] += 1
                if pos[1] >= len(map):
                    pos[1] = 0
            if map[pos[1]][pos[0]] == ' ':
                pos[1] += 1
                if pos[1] >= len(map):
                    pos[1] = 0
                    while map[pos[1]][pos[0]] != ' ':
                        pos[1] += 1
                pos[1] -= 1
        elif dir == 'D':
            pos[1] += 1
            if pos[1] >= len(map):
                pos[1] = 0
            if map[pos[1]][pos[0]] != '.':
                pos[1] -= 1
                if pos[1] < 0:
                    pos[1] = len(map) - 1
            if map[pos[1]][pos[0]] == ' ':
                pos[1] -= 1
                if pos[1] < 0:
                    pos[1] = len(map) - 1
                    while map[pos[1]][pos[0]] != ' ':
                        pos[1] -= 1
                pos[1] += 1
        else:
            raise Exception('Invalid direction')
        """

def turn(dir):
    global d
    ## dir can be (L)eft or (R)ight
    if dir == 'R':
        d = [-d[1], d[0]]
    elif dir == 'L':
        d = [d[1], -d[0]]

## your code goes here
if p == 2: ## part 2
    ## parse each side in this format:
    #.U.
    #LFR
    #.D.
    #.B.
    sides = {}
    for i in range(0, len(lines), 11):
        tile = int(lines[i][5:9])
        sides[tile] = []
        for j in range(1, 11):
            sides[tile].append(lines[i+j])
    print(sides)

for step, dir in instructions:
    move(step, d)
    turn(dir)
# facing - 0 for right, 1 for down, 2 for left, 3 for up
facing = 'a'
if d[0] == 1:
    facing = 0
elif d[0] == -1:
    facing = 2
elif d[1] == 1:
    facing = 1
elif d[1] == -1:
    facing = 3
assert type(facing) == int
print(pos)
ans = 1000*(pos[1]+1) + 4*(pos[0]+1) + facing
# ans = 1337


## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)
# real_print(d)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
