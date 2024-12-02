#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

## you don't want to print a lot of debug info if you aren't in debug mode!
real_print = print
if not d:
    print = lambda *args, **kwargs: None

# some helpful information:
# the variable p stores what part you are currently on, it's either 1 or 2
# make your script work with both parts by using if p == 1: ... else: ...
# the variable d is a boolean; it returns if you are in debug mode or not
# the submit function works 
# the variable t is a boolean; it returns if you are in test mode or not
ans = 'No answer calculated yet'

blizzards = []
for y in rl(lines):
    for x in rl(lines[y]):
        if lines[y][x] in '>v<^>':
            blizzards.append((x,y,lines[y][x]))


paths = [[(1,0)]]

def getDirMapping(d):
    # > for left, v for down
    if d == '>': return (1, 0)
    elif d == 'v': return (0, 1)
    elif d == '<': return (-1, 0)
    elif d == '^': return (0, -1)

def getPoint(x,y):
    try:
        return lines[y][x]
    except Exception as e:
        print(f"point {x},{y} not found")
        raise e


def step(expect=(len(lines[0])-2,len(lines)-1)):
    global blitzards, paths, curRound
    print('expecting', expect)
    real_print(f"Number of paths: {len(paths)}")
    for _ in rl(blizzards):
        x, y, d = blizzards[_]
        dx, dy = getDirMapping(d)
        nx, ny = x+dx, y+dy
        if getPoint(nx, ny) != '#':
            blizzards[_] = (nx, ny, d)
        else:
            blizzards[_] = (
                    1 if dx == 1 else len(lines[0])-2 if dx == -1 else x,
                    1 if dy == 1 else len(lines)-2 if dy == -1 else y,
                    d)
    nps = []
    for _ in rl(paths):
        x, y = paths[_][-1]
        for d in [(0,0),(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x+d[0], y+d[1]
            inBlizzard = False
            for b in blizzards:
                if b[0] == nx and b[1] == ny:
                    #print('inside blizzard')
                    inBlizzard = True
                    break
            #print('not inside blizzard')
            if inBlizzard or nx < 0 or nx > len(lines[0])-1 or ny < 0 or ny > len(lines)-1 or lines[ny][nx] == '#': continue
            #print('not inside blizzard right?')
            alreadyInPath = False
            for p in nps:
                if p[-1][0] == nx and p[-1][1] == ny:
                    alreadyInPath = True
                    break
            if alreadyInPath: continue
            #if curRound == 18: print(f"Adding {nx},{ny} to path {_}")
            #if curRound == 19: exit()
            nps.append(paths[_] + [(nx,ny)])
            #print(len(lines[ny])-2, len(lines)-1)
            if nx == expect[0] and ny == expect[1]:
                print('found path', paths[_] + [(nx, ny)])
                paths= [[(nx, ny)]]
                return True

    paths=nps
    return False

print(blizzards)
curRound=0
while 1:
    curRound+=1
    real_print(f'Round {curRound}')
    if step(): break
    print(blizzards)
## your code goes here
if p == 1:
    # ans = 1337
    pass
else: ## part 2
    # ans = 13371337
    while 1:
        curRound+=1
        real_print(f'Round {curRound}')
        if step(expect=(1,0)): break
        print(blizzards)

    while 1:
        curRound+=1
        real_print(f'Round {curRound}')
        if step(): break
        print(blizzards)
    pass

ans=curRound
## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
