#!/bin/python3

import sys
inp = sys.stdin.read()
lines = inp.splitlines()
rock_paths = [[[int(n) for n in p.split(',')] for p in line.split(' -> ')] for line in lines]

board = {}

def stepify(distance):
    if distance == 0:
        return 0
    if distance > 0:
        return 1
    return -1

for rock_path in rock_paths:
    rp = rock_path
    cur_pos = rp[0]
    for coord in rp[1:]:
        while cur_pos != coord:
            board[tuple(cur_pos)] = '#'
            cur_pos[0] += stepify(coord[0] - cur_pos[0])
            cur_pos[1] += stepify(coord[1] - cur_pos[1])
    board[tuple(cur_pos)] = '#'

#for x, y in [(1,0),(2,1),(0,2),(1,2),(2,2)]:
#    board[x,y] = '#'

def min_max(nums):
    return min(nums), max(nums)

minx, maxx = min_max([x for x, _ in board])
miny, maxy = min_max([y for _, y in board])

def print_board(board):
    global minx, maxx, miny, maxy
    minx, maxx = min_max([x for x, _ in board])
    miny, maxy = min_max([y for _, y in board])

    print()

    for digit in range(len(str(maxx))):
        print(' '*(1+len(str(maxx))), end='')
        for x in range(minx, maxx+1):
            print(str(x)[digit], end='')
        print()

    print(' '*(1+len(str(maxx))), end='')
    sand_drop_x = 500
    print(' '*(sand_drop_x-minx), end='')
    print('+')

    for y in range(miny-1, maxy+2):
        print(f"{('0'*(len(str(maxy+1))-len(str(y))))+str(y)} ", end='')
        for x in range(minx-1, maxx+2):
            c=board.get((x, y), ' ')
            print(c if c!='^' else '.', end='')
        print()

# Sand!!!
#board[500, 0] = '+'
_=0
fell_down_world = False
moved = False

while True:
    sand = (500, 0)

    while True:
        moved = False
        for new_sand in [(sand[0], sand[1]+1), (sand[0]-1, sand[1]+1), (sand[0]+1, sand[1]+1)]:
            if board.get(new_sand, '.') == '.' and new_sand[1] < maxy + 2:
                moved = True
                sand = new_sand
                break
        if not moved:
            board[tuple(sand)] = '^'#chr(ord('a') + _%26)
            _+=1
            if sand == (500, 0):
                fell_down_world = True
            break

    if fell_down_world:
        break

print_board(board)
print(miny-1)
print(fell_down_world,_)
