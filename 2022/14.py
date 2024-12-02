#!/bin/python3
import time, sys
inp = sys.stdin.read()
lines = inp.splitlines()

visualize = 0
alphabet = 0
part = 1

args = sys.argv[1:]
# flags: v = visualize, a = alphabetize, 2 = part 2
for arg in args:
    if 'v' in arg:
        visualize = 1
    if 'a' in arg:
        alphabet = 1
    if '2' in arg:
        part = 2


alphabetize = lambda n: chr(ord('a') + n%26) if n%(26*2) < 26 else chr(ord('A') + n%26)

def print_visualization():
    global old_board, new_board
    visual_board = board.copy()
    visual_board[sand] = alphabetize(_) if alphabet else '+'
    new_board = print_board(visual_board,ret=True)
    #print("round %d" % _)
    if old_board is None:
        # print escape sequence to clear screen
        print('\033[2J', end='')
        # now print each line
        for y in range(len(new_board.splitlines())):
            # move cursor to beginning of line
            print(f"\033[{y};0H")
            print(new_board.splitlines()[y])
    elif new_board != old_board:
        # find difference between old and new, x and y positions
        #print(len(new_board) == len(old_board))
        #print(len(new_board.splitlines()) == len(old_board.splitlines()))
        for y, (new_line, old_line) in enumerate(zip(new_board.splitlines(), old_board.splitlines())):
            if new_line != old_line:
                for x in range(len(new_line)):
                    if len(new_line) != len(old_line):
                        print(f"\033[{y+1};{0}H", end=new_line)
                        continue
                    if new_line[x] != old_line[x]:
                        #print("difference at (%d, %d)" % (x, y))
                        #print("difference is %c vs %c" % (new_line[x], old_line[x]))
                        print(f"\033[{y+1};{x+1}H", end=new_line[x])
                #print(y, new_line)
                #print(y, old_line)
                #print()
    # move cursor to (0, 0)
    print("\033[0;0H", end='')
    ## flush stdout
    sys.stdout.flush()
    time.sleep(0.03)

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

def print_board(board,ret=False):
    global minx, maxx, miny, maxy
    min_x, max_x = min_max([x for x, _ in board])
    min_y, max_y = min_max([y for _, y in board])

    minx = min(min_x, minx)
    maxx = max(max_x, maxx)
    miny = min(min_y+1, miny)

    out = ''

    if ret:
        def pprint(*args, **kwargs):
            nonlocal out
            out += ''.join(map(str,args))
            if len(args) == 0:
                out += '\n'
            return out
    else:
        pprint = print
    pprint('\n')

    x_offset=len(str(maxy+1))+2
    
    for digit in range(len(str(maxx))):
        pprint(' '*x_offset, end='')
        for x in range(min(minx,500), max(maxx+1, 500)):
            pprint(str(x)[digit], end='')
        pprint()

    pprint(' '*x_offset, end='')
    sand_drop_x = 500
    pprint(' '*(sand_drop_x-minx), end='')
    pprint('+')
    pprint()

    for y in range(miny-1, maxy+2):
        pprint(f"{('0'*(len(str(maxy+1))-len(str(y))))+str(y)} ", end='')
        for x in range(minx-1, maxx+2):
            c=board.get((x, y), ' ')
            pprint(c if c!='^' else '.', end='')
        pprint()
    if ret:
        return out

# Sand!!!
#board[500, 0] = '+'
_=0
fell_down_world = False
moved = False
old_board = None
new_board = None
while True:
    sand = (500, 0)

    while True:
        if visualize and sand[1] >= miny-1:
            print_visualization()
            old_board = new_board
        moved = False
        for new_sand in [(sand[0], sand[1]+1), (sand[0]-1, sand[1]+1), (sand[0]+1, sand[1]+1)]:
            if board.get(new_sand, '.') == '.' and (part == 1 or new_sand[1] < maxy + 2):
                moved = True
                sand = new_sand
                break
        if part == 1 and sand[1] >= maxy:
            fell_down_world = True
            break
        if not moved:
            board[tuple(sand)] = alphabetize(_) if alphabet else '^'
            _+=1
            if part == 2 and sand == (500, 0):
                fell_down_world = True
            break

    if fell_down_world:
        board[tuple(sand)] = alphabetize(_) if alphabet else '^'
        break

print()
if visualize:
    print_visualization()
    ## go to last line with escape sequence
    print(f"\033[{len(new_board.splitlines())};0H", end='')
else:
    print_board(board)
print(f"Part {part}:", _)
#print("Also part 1:", sum(1 for k, v in board.items() if v == '^'))
