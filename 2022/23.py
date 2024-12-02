#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

## you don't want to print a lot of debug info if you aren't in debug mode!
if not d:
    real_print = print
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

# some helpful information:
# the variable p stores what part you are currently on, it's either 1 or 2
# make your script work with both parts by using if p == 1: ... else: ...
# the variable d is a boolean; it returns if you are in debug mode or not
# the submit function works 
# the variable t is a boolean; it returns if you are in test mode or not
ans = 'No answer calculated yet'

map = {}
for y in rl(lines):
    for x in rl(lines[y]):
        map[(x,y)] = lines[y][x]
def getPoint(x,y,d=False):
    try:
        if d: print(x,y,map[(x,y)],'from getPoint')
        return map[(x,y)]
    except Exception as e:
        if d: print(sys.exc_info(), 'fuckin error')
        return '.'
def getDirMapping(d):
    # (N, E, S, W)
    if d == 'N':
        return (0, -1)
    elif d == 'E':
        return (1, 0)
    elif d == 'S':
        return (0, 1)
    elif d == 'W':
        return (-1, 0)
dirs = ['N', 'S', 'W', 'E']

#addPosToMap = lambda pos, map: '\n'.join(map[max(0,pos[1]-2):pos[1]] + [map[pos[1]][:pos[0]] + 'X' + map[pos[1]][pos[0]+1:]] + map[pos[1]+1:pos[1]+3])
#addPosToMap = lambda pos, map: '\n'.join(map[:pos[1]] + [map[pos[1]][:pos[0]] + 'X' + map[pos[1]][pos[0]+1:]] + map[pos[1]+1:])
# check:
# #######
# .DDEDD.
# where E is elf
# and # is wall
# and D is different elf
# and . is empty space
# rotate check for the right direction
def check(x, y, d, a = 0):
    toCheck = [(-1, -1), (0, -1), (1, -1)] 
    for _ in rl(toCheck):
        dx, dy = getDirMapping(d)
        if dx == -1:
            toCheck[_] = (toCheck[_][1], toCheck[_][0])
        elif dy == 1:
            toCheck[_] = (toCheck[_][0], -toCheck[_][1])
        elif dx == 1:
            toCheck[_] = (-toCheck[_][1], toCheck[_][0])

    checkPass = True
    if a: print(dx, dy, toCheck)
    for _ in rl(toCheck):
        if a: print(toCheck[_][0]+x, toCheck[_][1]+y, getPoint(x+toCheck[_][0], y+toCheck[_][0]))

        if getPoint(x+toCheck[_][0], y+toCheck[_][1], d=a) != '.':
            checkPass = False
    if a: print(checkPass)
    return checkPass

## your code goes here
oldmap = map.copy()
# ans = 1337
print('round 0')
print_board(map)
debug=d
for _ in range(10 if p == 1 else 99999):
    if not debug:
        # use zfill
        print('round', )
        sys.stdout.write("\r" + f'round {str(_+1).zfill(5)}')
        sys.stdout.flush()

    proposed_moves = {}
    for x, y in map:
        a = 0#x == 2 and y == 1
        if map[(x,y)] != '#':
            continue
        shouldIMove = False
        for d in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
            if getPoint(x+d[0], y+d[1]) == '#':
                shouldIMove = True
        if not shouldIMove:
            if a: print('aaaa')
            continue
        for dir in dirs:
            if check(x, y, dir, a=a):
                dx, dy = getDirMapping(dir)
                if (x+dx, y+dy) not in proposed_moves:
                    proposed_moves[(x+dx, y+dy)] = (x, y, dir)
                else:
                    print(x, y, dir, 'already in proposed moves')
                    proposed_moves[(x+dx, y+dy)] = ('invalid', 'invalid', 'invalid')
                break
    #print(proposed_moves)
    for move in proposed_moves:
        x, y, dir = proposed_moves[move]
        if x == 'invalid':
            continue
        map[move] = '#'
        try: del map[(x,y)]
        except: pass
    print(f'round {_+1}')

    print_board(map)

    dirs.append(dirs.pop(0))
    print(dirs)
    if map == oldmap:
        if p == 2: ans = _+1
        break
    oldmap = map.copy()
if p == 1:
    minx, maxx = min_max([x for x, _ in map])
    miny, maxy = min_max([y for _, y in map])
    print(minx, maxx, miny, maxy)
    ans = 0
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if getPoint(x,y) == '.':
                ans += 1

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)
real_print()

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
